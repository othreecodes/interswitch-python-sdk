from constants import Constants
import base64
import requests
from exceptions import InterswitchAPIException
from request_headers import RequestHeaders
from constants import Constants
import utils


class InterSwitchAPI(object):
    def __init__(self, client_secret, client_id, env, terminal_id) -> None:

        self.client_secret = client_secret
        self.client_id = client_id
        self.terminal_id = terminal_id
        if env == Constants.ENV_SANDBOX:
            self.base_url = Constants.SANDBOX_BASE_URL
        elif env == Constants.DEV_BASE_URL:
            self.base_url = Constants.DEV_BASE_URL
        elif env == Constants.PRODUCTION_BASE_URL:
            self.base_url = Constants.PRODUCTION_BASE_URL

    def get_client_access_token(self):
        passport_url = self.base_url + Constants.PASSPORT_RESOURCE_URL
        auth_cipher = self.client_id + ":" + self.client_secret
        basic_auth = base64.encodebytes(bytes(auth_cipher, "utf-8"))
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic {}".format(
                basic_auth.decode("utf-8").strip().replace("\n", "")
            ),
        }
        payload = {"grant_type": "client_credentials"}
        response = requests.post(passport_url, data=payload, headers=headers)

        if response.status_code == 200:
            return response.json()["access_token"]
        else:
            raise InterswitchAPIException(response.json()["description"])

    def get_billers(self):
        url = self.base_url + Constants.QT_BASE_URL + Constants.BILLERS_URL
        headers = {Constants.TERMINAL_ID: self.terminal_id}

        response = self.make_request(url, "GET", None, headers)

        return response

    def get_bank_codes(self):
        url = self.base_url + Constants.QT_BASE_URL + Constants.BANK_CODES_URL
        headers = {Constants.TERMINAL_ID: self.terminal_id}

        response = self.make_request(url, "GET", None, headers)

        return response
        # 011

    def name_enquiry(self, bank_code, account_number):

        url = self.base_url + Constants.NAME_ENQUIRY_URL
        headers = {Constants.BANK_CODE: bank_code, Constants.ACCOUNT_ID: account_number}

        response = self.make_request(url, "GET", None, headers)
        return response

    def transfer_funds(
        self,
        initiating_entity_code,
        sender_last_name,
        sender_other_names,
        beneficiary_last_name,
        beneficiary_other_names,
        initiation_amount,
        initiation_channel,
        initiation_payment_method_code,
        initiation_currency_code,
        terminaing_paymet_method_code,
        terminating_amount,
        terminating_currency_code,
        terminating_country_code,
        terminating_account_number,
        terminating_account_type,
        terminaing_entity_code,
    ):
        """
        Documentation: https://sandbox.interswitchng.com/docbase/docs/quickteller-sva/funds-transfer/
        """
        url = self.base_url + Constants.QT_BASE_URL + Constants.TRANSFER_FUNDS_URL
        headers = {Constants.TERMINAL_ID: self.terminal_id}

        data = {
            "mac": utils.generate_mac(
                initiation_amount,
                initiation_currency_code,
                initiation_payment_method_code,
                terminating_amount,
                terminating_currency_code,
                terminaing_paymet_method_code,
                terminating_country_code,
            ),
            "beneficiary": {
                "lastname": beneficiary_last_name,
                "othernames": beneficiary_other_names,
            },
            "initiatingEntityCode": initiating_entity_code,
            "initiation": {
                "amount": initiation_amount,
                "channel": initiation_channel,
                "currencyCode": initiation_currency_code,
                "paymentMethodCode": initiation_payment_method_code,
            },
            "sender": {"lastname": sender_last_name, "othernames": sender_other_names},
            "termination": {
                "accountReceivable": {
                    "accountNumber": terminating_account_number,
                    "accountType": terminating_account_type,
                },
                "amount": terminating_amount,
                "countryCode": terminating_country_code,
                "currencyCode": terminating_currency_code,
                "entityCode": terminaing_entity_code,
                "paymentMethodCode": terminaing_paymet_method_code,
            },
            "transferCode": "1413{}".format(utils.generate_timestamp()),
        }

        response = self.make_request(url, "POST", data, headers)
        return response

    def transfer_to_nigerain_account(
        self,
        sender_last_name,
        sender_other_names,
        beneficiary_last_name,
        beneficiary_other_names,
        account_number,
        bank_code,
        account_type,
        amount
    ):

        return self.transfer_funds(
            initiating_entity_code="ERT",
            sender_last_name=sender_last_name,
            sender_other_names=sender_other_names,
            beneficiary_last_name=beneficiary_last_name,
            beneficiary_other_names=beneficiary_other_names,
            initiation_amount=amount,
            initiation_channel="7",
            initiation_payment_method_code="CA",
            initiation_currency_code="566",
            terminaing_paymet_method_code="AC",
            terminating_amount=amount,
            terminating_currency_code="566",
            terminating_country_code="NG",
            terminating_account_number=account_number,
            terminating_account_type=account_type,
            terminaing_entity_code=bank_code,
        )

    def make_request(self, url, method, data, extra_headers):

        access_token = self.get_client_access_token()

        headers = RequestHeaders.beader_security_request_headers(
            self.client_id, self.client_secret, access_token, url, method
        )

        if extra_headers != None:
            headers.update(extra_headers)

        if method == "GET":
            return requests.get(url, data=data, headers=headers).json()
        else:
            return requests.post(url, json=data, headers=headers).json()
