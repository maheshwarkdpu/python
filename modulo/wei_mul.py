#! /usr/bin/python3.6
import sys
from ecc_lib import *
#from montgomery_to_weierstreass1 import *


#montgomery constants in Weierstrass form
p =  0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed
a =  0x2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa984914a144
b =  0x7b425ed097b425ed097b425ed097b425ed097b425ed097b4260b5e9c7710c864
order = 2**252 + 0x14def9dea2f79cd65812631a5cf5d3ed

#Gx = 0x2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad245a
#Gy = 0x20ae19a1b8a086b4e01edd2c7748d14c923d4d7e6d7c61b229e9c5a27eced3d9
#
##scalar = 0x77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a
#scalar = 0x5dab087e624a8a4b79e17f8b83800ee66f3bb1292618b6fd1c2f8b27ff88e0eb

Gx = 0x79d63319bf29a757f812230672ee2de9e1e08f976d0c067e5f6c28262888c32f
Gy = 0x29973f8fd61dd2d3f670b1a2b55e9d5712d1fc2070fc7014af56be3bb016d90
scalar = 0x77076d0a7318a57d3c16c17251b26645df4c2f87ebc0992ab177fba51db92c2a 



#Gx = 0x76c7567b50ae53bae5e05dd196cf111d270a5bcf4f6c3ee085dadb0312160037
#Gy = 0x9a452b201ddcd02e0c9635bd4a1bc859013d1a68c4174c1ee652b07205901b8
#scalar = 0xa546e36bf0527c9d3b16154b82465edd62144c0ac1fc5a18506a2244ba449ac4

#Gx = 0x3e4ec071f47ff7a6e8e76b19bb9285dbd758e2b04840629f7dbc1322bcbc4649
#Gy = 0x3bd04c2029a0dd7f6461010a1a87931cc5dfef782089f7ea3dc47f2093ba65bb
#scalar = 0x4b66e9d4d1b4673c5ad22691957d6af5c11b6421e0ea01d42ca4169e7918ba0d


Gz = 0x1

byte_scalar = scalar.to_bytes(32,byteorder='little')
int_scalar = int.from_bytes(byte_scalar, byteorder='big')
print("\n scalar after big_num : ",hex(int_scalar))
print("\n\n")

# masking as per Montgomery mul
mask1 = 0x4000000000000000000000000000000000000000000000000000000000000000
mask2 = 0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8
int_scalar = int_scalar | mask1
int_scalar = int_scalar & mask2

print("scalar after masking : ", hex(int_scalar))



rx, ry, rz = ecc_mul(Gx, Gy, Gz, int_scalar, a, p)
inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
ry = (ry * inv_rz)%p
Qx = rx
Qy = ry
Qz = (rz * inv_rz)%p
print(" Qx = ", hex(Qx))
print(" Qy = ", hex(Qy))
print(" Qz = ", hex(Qz))
