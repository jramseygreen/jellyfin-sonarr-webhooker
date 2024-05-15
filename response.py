from flask import make_response, jsonify

class __Response:
    # standardise all responses
    def _formatted_response(self, message: str = None, data=None, status: int = 200, error_type=None):
        response_data = {
            'message': message,
            'data': data,
            'success': True,
            'status': status
        }

        if status >= 400:
            response_data['success'] = False
            response_data['error_type'] = 'client_error'

        if status >= 500:
            response_data['error_type'] = 'server_error'

        if error_type:
            response_data['error_type'] = error_type


        response = make_response(jsonify(response_data), status)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Informational responses (100-199)
    def continue_(self):
        return self._formatted_response(status=100)

    def switching_protocols(self):
        return self._formatted_response(status=101)

    # Successful responses (200-299)
    def ok(self, message: str = None, data=None):
        return self._formatted_response(message, data, 200)

    def created(self, message: str = None, data=None):
        return self._formatted_response(message, data, 201)

    def accepted(self, message: str = None, data=None):
        return self._formatted_response(message, data, 202)

    def non_authoritative_information(self, message: str = None, data=None):
        return self._formatted_response(message, data, 203)

    def no_content(self, message: str = None, data=None):
        return self._formatted_response(message, data, 204)

    def reset_content(self, message: str = None, data=None):
        return self._formatted_response(message, data, 205)

    def partial_content(self, message: str = None, data=None):
        return self._formatted_response(message, data, 206)

    # Redirection responses (300-399)
    def multiple_choices(self, message: str = None, data=None):
        return self._formatted_response(message, data, 300)

    def moved_permanently(self, message: str = None, data=None):
        return self._formatted_response(message, data, 301)

    def found(self, message: str = None, data=None):
        return self._formatted_response(message, data, 302)

    def see_other(self, message: str = None, data=None):
        return self._formatted_response(message, data, 303)

    def not_modified(self, message: str = None, data=None):
        return self._formatted_response(message, data, 304)

    def use_proxy(self, message: str = None, data=None):
        return self._formatted_response(message, data, 305)

    def temporary_redirect(self, message: str = None, data=None):
        return self._formatted_response(message, data, 307)

    def permanent_redirect(self, message: str = None, data=None):
        return self._formatted_response(message, data, 308)

    # Client error responses (400-499)
    def bad_request(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 400, error_type)

    def unauthorized(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 401, error_type)

    def payment_required(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 402, error_type)

    def forbidden(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 403, error_type)

    def not_found(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 404, error_type)

    def method_not_allowed(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 405, error_type)

    def not_acceptable(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 406, error_type)

    def proxy_authentication_required(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 407, error_type)

    def request_timeout(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 408, error_type)

    def conflict(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 409, error_type)

    def gone(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 410, error_type)

    def length_required(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 411, error_type)

    def precondition_failed(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 412, error_type)

    def payload_too_large(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 413, error_type)

    def uri_too_long(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 414, error_type)

    def unsupported_media_type(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 415, error_type)

    def range_not_satisfiable(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 416, error_type)

    def expectation_failed(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 417, error_type)

    def im_a_teapot(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 418, error_type)

    # Server error responses (500-599)
    def internal_server_error(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 500, error_type)

    def not_implemented(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 501, error_type)

    def bad_gateway(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 502, error_type)

    def service_unavailable(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 503, error_type)

    def gateway_timeout(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 504, error_type)

    def http_version_not_supported(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 505, error_type)

    def variant_also_negotiates(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 506, error_type)

    def insufficient_storage(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 507, error_type)

    def loop_detected(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 508, error_type)

    def not_extended(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 510, error_type)

    def network_authentication_required(self, message: str = None, data=None, error_type=None):
        return self._formatted_response(message, data, 511, error_type)

response = __Response()
