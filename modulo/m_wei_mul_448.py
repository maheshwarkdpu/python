#! /usr/bin/python3.6
import sys
from ecc_lib import *

#Curve 448 constants
p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffff
a = 0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa9fffffffffffffffffffffffffffffffffffffffffffffffe1a76d41f
b = 0x5ed097b425ed097b425ed097b425ed097b425ed097b425ed097b425e71c71c71c71c71c71c71c71c71c71c71c71c71c71c72c87b7cc69f70
order = 2**446 -  0x8335dc163bb124b65129c96fde933d8d723a70aadc873d6d54a7bb0d

#base point 5
#Gx =  0xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa0000000000000000000000000000000000000000000000000000cb91
#Gy =  0x82dca2ed6a0a4e0993675491a7cd90313451a2cb0aaaba2f9f08a23c720c091247fd81dcb9bcf2deeced3b4eaf9885089028ddc2ba84a4e5

# X448(a, 5)
#Gx = 0x4aca6edd902b29c1fdb7bd3384bd05b77efe83ec1d0ee17366846fcd2c3da7fa639ce03db8d23b274a0721a1aed5227de6e3b731ccf7d428
#Gy = 0x1e6ad20877b43b4f5d394e18f767fa6c44e428e02f69f98b8fe6be65594cea520d930b3d68c9d5e77c852e97bd112c25b040a11f98d8d9cb

# X448(b, 5)
Gx = 0xb3e19e26716c67b258e897256086b151e74bdceda5dee9a71d6482d130b445f3d4b0bd077162a46dcfec6f9b590bfcbcf520cdb029a982ca
Gy = 0xdbf174e689970aa79bbe1f9401689374a8339de9c250ef3d9d93907f7476e83523dd01e65b9a282e3906d6ff4f70bdc1fa3f8219328f6dab


Gz = 0x1

#Test vector - 1, a
scalar = 0x9a8f4925d1519f5775cf46b04b5800d4ee9ee8bae8bc5565d498c28dd9c9baf574a9419744897391006382a6f127ab1d9ac2d8c0a598726b

#Test vector - 2, b
#scalar = 0x1c306a7ac2a0e2e0990b294470cba339e6453772b075811d8fad0d1d6927c120bb5ee8972b0d3e21374c9c921b09d1b0366f10b65173992d

#Test vector - 2
#scalar = 0x3eb7a829b0cd20f5bcfc0b599b6feccf6da4627107bdb0d4f345b43027d8b972fc3e34fb4232a13ca706dcb57aec3dae07bdc1c67bf33609


print("\n scalar before big_num : ",hex(scalar))
byte_scalar = scalar.to_bytes(56,byteorder='little')
int_scalar = int.from_bytes(byte_scalar, byteorder='big')
print("\n scalar after big_num : ",hex(int_scalar))
print("\n\n")

# masking as per Montgomery mul
mask1 = 0x8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
mask2 = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffC
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
