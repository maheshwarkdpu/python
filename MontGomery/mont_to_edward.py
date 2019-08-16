

from ecc_lib import *


# Montgomery (u,v) coordinates to Edwarad (x,y) coordinate converstion.
# (x, y) = (sqrt(-486664)*u/v, (u-1)/(u+1))



p = 2**255  - 19
#u = 9
u=0x478dd307cdfb042d80d03e0f55227e4d982bedd1696ba700fc8ab894c504c725

minus_u = -u % p
print("\n")
print("     decimal         u = ",u)
print(" hexadecimal         u = ",hex(u))
print("     decimal   minus_u = ",minus_u)
print(" hexadecimal   minus_u = ",hex(minus_u))

u3 = (u*u*u)%p
Au2 = (486662*u*u)%p
u_result = (u3 + Au2 + u)%p
sqrt_u  = sqrt_25519(u_result)
v = sqrt_u
v = -v%p
minus_v = -v%p
print("\n")
print("     decimal          v = ",v)
print(" hexadecimal          v = ",hex(v))
print("     decimal    minus_v = ",minus_v)
print(" hexadecimal    minus_v = ",hex(minus_v))
print("\n")




# Montgomery (u,v) coordinates to Edwarad (x,y) coordinate converstion.
# (x, y) = (sqrt(-486664)*u/v, (u-1)/(u+1))
A = 486664
minus_A = -A
minus_A = minus_A % p
sqrt_A  = sqrt_25519(minus_A)
inverse_v = pow(v, (p-2), p)

x = (sqrt_A * u * inverse_v) % p

minus_x = -x
minus_x = -x % p


um1 = u-1
up1 = u+1

inverse_up1  =  pow(up1, (p-2), p)

y = (um1 * inverse_up1) % p
minus_y = -y % p



print(" x           decimal   = ",x)
print(" x       hexadecimal   = ",hex(x))
print(" y           decimal   = ",y)
print(" y       hexadecimal   = ",hex(y))

print(" minus_x     decimal   = ",minus_x)
print(" minus_x hexadecimal   = ",hex(minus_x))
print(" minus_y     decimal   = ",minus_y)
print(" minus_y hexadecimal   = ",hex(minus_y))




