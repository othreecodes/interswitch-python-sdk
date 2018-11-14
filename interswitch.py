class InterSwitchAPI(object):


    def __init__(self, api_key, client_id) -> None:
        assert api_key is not None
        self.api_key = api_key
        self.client_id = client_id

