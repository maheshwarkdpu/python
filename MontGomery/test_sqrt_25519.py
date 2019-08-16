

from ecc_lib import *




p = 2**255  - 19

x_0 = 0
a = 0x21a17a26452fc5bcf192ba3ba3a7a0c4cf8d69b1c4b981d4294f1683bd3ecd0f
a = 0x1c724e24da5451bd28118553a12b6a8586ba022a43a359e9e8e60a369b97b876
print("\n (a):  ", hex(a))
b = sqrt_25519(a)
print("\n sqrt_25519(a):  : ",hex(b))
#if(x_0 != (b&1)):
#    b = p - b
#print("\n sqrt_25519(a):  : ",hex(b))
print()


