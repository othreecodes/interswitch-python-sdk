import time
import uuid
import base64
import hashlib


def get_nonce():
    return str(uuid.uuid4()).replace("-", "")


def generate_timestamp():
    return int(time.time())


def hash_sha1(val):
    return base64.b64encode(hashlib.sha1(val).digest())


def hash_sha1_only(val):
    return hashlib.sha1(val).digest()


def generate_mac(a,b,c,d,e,f,g):
    
    data = hashlib.sha512("{}{}{}{}{}{}{}".format(a,b,c,d,e,f,g).encode('utf-8')).hexdigest()
   
    return data