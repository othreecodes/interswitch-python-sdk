from constants import Constants
from . import utils


def _get_signature(client_id, client_secret_key, resource_url, http_method, timestamp, transaction_params):
    pass


class RequestHeaders(object):

    @staticmethod
    def beader_security_request_headers(client_id, client_secret_key, resource_url, http_method, timestamp,
                                        transaction_params) -> dict:
        headers = {}

        headers[Constants.NONCE] = utils.get_nonce()
        headers[Constants.SIGNATURE] = _get_signature(client_id, client_secret_key, resource_url, http_method,
                                                      timestamp, transaction_params)

        return headers
