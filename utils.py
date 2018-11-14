import time
import uuid


def get_nonce():
    return str(uuid.uuid4()).replace("-", "")


def generate_timestamp():
    return int(time.time())
