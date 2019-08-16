#! /usr/bin/python

import hashlib


a = 0x0000000000000000000000000000000000000000000000000000000000000001
for i in range(1,257):

    #print("a = ",hex(a))
    b = int.to_bytes(a,32,'big')
    print("b = ",b)
    h = hashlib.sha256(b)
    print("a =",hex(a)," Hash(a) = ",h.hexdigest())
    a = a << 1
    #print(" -------------------------------------------------------------------------------------------")
print()




