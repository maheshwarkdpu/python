#! /usr/bin/python



import sys
import binascii

from eddsa2 import Ed25519
debug=1

def munge_string(s, pos, change):
    return (s[:pos] +
            int.to_bytes(s[pos] ^ change, 1, "little") +
            s[pos+1:])
# Read a file in the format of
# http://ed25519.cr.yp.to/python/sign.input
lineno = 0
while True:
    #print("\n I am in sign.py  ------------ start\n");
    line = sys.stdin.readline()
    if not line:
        break
    lineno = lineno + 1
    print(lineno)
    #print(type(line))
    fields = line.split(":")
    if(debug):
        print("\n fields : ",fields)

    secret = (binascii.unhexlify(fields[0]))[:32]
    if(debug):
        print("\n secret : ",secret.hex())

    public = binascii.unhexlify(fields[1])
    if(debug):
        print("\n public : ",public.hex())

    msg = binascii.unhexlify(fields[2])
    if(debug):
        print("\n msg : ",msg.hex())

    signature = binascii.unhexlify(fields[3])[:64]
    if(debug):
        print("\n signature : ",signature.hex())

    privkey,pubkey = Ed25519.keygen(secret)
    if(debug):
        print(" type(privkey) = ", type(privkey))
        print(" type(pubkey) = ", type(pubkey))
    assert public == pubkey
    assert signature == Ed25519.sign(privkey, pubkey, msg)
    if(debug):
        print("\n verify start : ")
    assert Ed25519.verify(public, msg, signature)
    if(debug):
        print("\n verify end : ")
    if len(msg) == 0:
        bad_msg = b"x"
    else:
        bad_msg = munge_string(msg, len(msg) // 3, 4)
    assert not Ed25519.verify(public,bad_msg,signature)
    assert not Ed25519.verify(public, msg, munge_string(signature,20,8))
    assert not Ed25519.verify(public,msg,munge_string(signature,40,16))

#print("\n I am in sign.py  ------------ end \n");


