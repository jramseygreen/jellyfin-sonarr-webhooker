from flask import Flask, request
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher
from threading import Thread
from cheroot.ssl.builtin import BuiltinSSLAdapter

class Server:
    def __init__(self, host: str = 'localhost', port: int = 8080, spa_path: str = 'frontend/dist',
                 index_file: str = 'index.html', ssl_cert: str = None, ssl_key:str = None, num_workers = 1):
        self.__server = None
        self.__host = host
        self.__port = port
        self.__app = Flask(__file__, static_folder=spa_path, static_url_path='/')
        self.__spa_path = spa_path
        self.__index_file = index_file
        self.__error_handlers = []
        self.__ssl_cert = ssl_cert
        self.__ssl_key = ssl_key
        self.__num_workers = num_workers

    def initialize(self):
        # sort in order of the number of / in the route prefix
        sorted_error_handlers = sorted(self.__error_handlers, key=lambda  x: x['route_prefix'].count('/'), reverse=True)

        # catches all error codes
        @self.__app.errorhandler(Exception)
        def catch_all(e):
            if getattr(e, 'code', None):
                for error_handler in sorted_error_handlers:
                    if request.path.startswith(error_handler['route_prefix']) and error_handler['error_code'] == e.code:
                        return error_handler['func'](e)

                # unless there is an override this runs
                # webserver always serves the spa unless there is a reason not to
                if e.code == 404:
                    return self.__app.send_static_file(self.__index_file)

            # else just default behaviour (return the error)
            return e

    def start(self, threading: bool = False):
        if threading:
            Thread(target=self.start).start()
            return
        if not self.__server:
            # cherrypy production webserver
            d = PathInfoDispatcher({'/': self.__app})  # load in flask app
            self.__server = WSGIServer((self.__host, self.__port), d, numthreads=self.__num_workers)  # create webserver with dispatcher

            # add https ssl if certificate and key exists
            if self.__ssl_cert and self.__ssl_key:
                self.__server.ssl_adapter =  BuiltinSSLAdapter(self.__ssl_cert, self.__ssl_key, None)

            try:
                print('Server started at  ', self.__host, ':', self.__port)
                self.__server.start()
            except KeyboardInterrupt:
                self.stop()

    def stop(self):
        if self.__server:
            self.__server.stop()
            self.__server = None
            print('Server stopped')

    def restart(self, threading: bool = False):
        self.stop()
        self.start()

    # use as decorator e.g. @server.errorhandler('/api', 404)
    def errorhandler(self, route_prefix: str, error_code: int):
        if not route_prefix[0] == '/':
            route_prefix = '/' + route_prefix

        if route_prefix[-1] == '/':
            route_prefix = route_prefix[:-1]

        def inner(func):
            self.__error_handlers.append({
                'route_prefix': route_prefix,
                'error_code': error_code,
                'func': func
            })
        return inner

    def register_blueprint(self, blueprint, url_prefix: str = ''):
        self.__app.register_blueprint(blueprint, url_prefix=url_prefix)

    def set_app_config(self, key: str, value):
        self.__app.config[key] = value

    def del_app_config(self, key: str):
        if key in self.__app.config:
            del self.__app.config[key]

    def get_app_config(self, key: str):
        if key in self.__app.config:
            return self.__app.config[key]

    def get_app(self) -> Flask:
        return self.__app

    def get_spa_path(self) -> str:
        return self.__spa_path

    def set_spa_path(self, spa_folder: str):
        self.__spa_path = spa_folder
        self.__app.static_folder = spa_folder

    def set_index_file(self, index_file: str):
        self.__index_file = index_file

    def get_host(self) -> str:
        return self.__host

    def get_port(self) -> int:
        return self.__port

    def set_host(self, host: str):
        self.__host = host
        if self.__server:
            self.restart()

    def set_port(self, port: int):
        self.__port = port
        if self.__server:
            self.restart()

    def set_ssl_cert(self, ssl_cert: str):
        self.__ssl_cert = ssl_cert

    def get_ssl_cert(self) -> str:
        return self.__ssl_cert

    def set_ssl_key(self, ssl_key: str):
        self.__ssl_key = ssl_key

    def get_ssl_key(self) -> str:
        return self.__ssl_key

    def set_num_workers(self, num_workers: int):
        self.__num_workers = num_workers

    def get_num_workers(self) -> int:
        return self.__num_workers

server = Server()
