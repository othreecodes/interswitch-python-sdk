from constants import Constants
import utils
import uuid
import time
import utils
from urllib import parse


def _get_signature(
    client_id, client_secret_key, resource_url: str, http_method, timestamp, nonce
):

    resource_url = parse.quote_plus(resource_url)

    signature_cipher = "{}&{}&{}&{}&{}&{}".format(
        http_method, resource_url, timestamp, nonce, client_id, client_secret_key
    )

    return utils.hash_sha1(str.encode(signature_cipher))


class RequestHeaders(object):
    @staticmethod
    def beader_security_request_headers(
        client_id, client_secret_key, access_token, resource_url, http_method
    ):
        headers = {}

        nonce = utils.get_nonce()
        headers[Constants.NONCE] = nonce
        timestamp = str(utils.generate_timestamp())
        headers[Constants.SIGNATURE] = _get_signature(
            client_id, client_secret_key, resource_url, http_method, timestamp, nonce
        )

        headers[Constants.SIGNATURE_METHOD] = Constants.SIGNATURE_METHOD_VALUE
        headers[Constants.TIMESTAMP] = timestamp
        headers[Constants.AUTHORIZATION] = (
            Constants.BEARER_AUTHORIZATION_REALM + " " + access_token
        )

        return headers
