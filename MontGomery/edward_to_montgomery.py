

from ecc_lib import *


# Montgomery (u,v) coordinates to Edwarad (x,y) coordinate converstion.
#(u, v) = ((1+y)/(1-y), sqrt(-486664)*u/x)

print("\n")
p = 2**255 - 19

x = 15112221349535400772501151409588531511454012693041857206046113283949847762202
y = 46316835694926478169428394003475163141307993866256225615783033603165251855960
minus_x = -x % p
minus_y = -y % p
print(" x           decimal   = ",x)
print(" x       hexadecimal   = ",hex(x))
print(" y           decimal   = ",y)
print(" y       hexadecimal   = ",hex(y))

print(" minus_x     decimal   = ",minus_x)
print(" minus_x hexadecimal   = ",hex(minus_x))
print(" minus_y     decimal   = ",minus_y)
print(" minus_y hexadecimal   = ",hex(minus_y))

one_plus_y = (1+y)%p
one_minus_y = (1-y)%p
inv_one_minus_y = pow(one_minus_y,(p-2),p)

u = (one_plus_y * inv_one_minus_y) % p

A = 486664
minus_A = -A
minus_A = minus_A % p
sqrt_A  = sqrt_25519(minus_A)
inverse_x = pow(x, (p-2), p)
v = (sqrt_A * u *  inverse_x) % p

print("\n After converting Edward to Montgomery :")
print("\n")
minus_u = -u % p
minus_v = -v%p
print("     decimal         u = ",u)
print(" hexadecimal         u = ",hex(u))
print("     decimal   minus_u = ",minus_u)
print(" hexadecimal   minus_u = ",hex(minus_u))
print("     decimal          v = ",v)
print(" hexadecimal          v = ",hex(v))
print("     decimal    minus_v = ",minus_v)
print(" hexadecimal    minus_v = ",hex(minus_v))
print("\n")




