
from  eddsa_lib import *

#p = 2**255  - 19
#print(" prime : ",hex(p))
#b = 256
#c = 3   # 2**c  ==>  2**3  ==> 8
#n = 254
#d = 0x52036cee2b6ffe738cc740797779e89800700a4d4141d8ab75eb4dca135978a3       # -121665/121666
#a = -1
#B = [0x216936d3cd6e53fec0a4e231fdd6dc5c692cc7609525a7b2c9562d608f25d51a, \
#        0x6666666666666666666666666666666666666666666666666666666666666658, \
#        0x01, \
#        0x67875f0fd78b766566ea4e8e64abe37d20f09f80775152f56dde8ab3a5b7dda3]  # X, Y, Z , T  ===>  T = (X*Y)%p
#
#L = 2^252+27742317777372353535851937790883648493
#
#
#pm1_by_4 = (p-1)//4
#print(hex(pm1_by_4))

secret = "9d61b19deffd5a60ba844af492ec2cc44449c5697b326919703bac031cae7f60"
msg = ""

RS = sign(secret,msg)

print("RS = ",hex(RS))
