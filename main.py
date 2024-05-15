from response import response
from server import Server
from api import api

from loader import config


api_base_url = '/api'

server = Server(host=config['host'], port=config['port'], spa_path='', num_workers=10)

server.register_blueprint(api, api_base_url)  # add a blueprint containing routes


# add a custom 404 method, fires when given route is request prefix
@server.errorhandler(api_base_url, 404)
def not_found(e):
    return response.not_found('Resource not found')

server.initialize()
server.start()
