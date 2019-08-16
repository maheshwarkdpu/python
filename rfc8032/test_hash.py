
from  eddsa_lib import *
from hashlib import *

secret = 0x4ccd089b28ff96da9db6c346ec114e0f5b8a319f35aba624da8cf6ed4fb8a6fb
msg = 0x72
byte_secret = secret.to_bytes(32,byteorder='big')
h = sha512(byte_secret)
print(h.hexdigest())

s = sign(secret, msg)


