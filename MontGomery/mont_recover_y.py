
from ecc_lib import *

# v^2  =  u^3  + 486662*u^2   +   u
# 
# v    =  sqrt(u^3  + 486662*u^2   +   u)
#
#   To find a square root of a, first compute the candidate root
#      x = a^((p+3)/8) (mod p).  Then there are three cases:
#
#      x^2 = a (mod p).  Then x is a square root.
#
#      x^2 = -a (mod p).  Then 2^((p-1)/4) * x is a square root.
#
#      a is not a square modulo p.
#

p = 2**255  - 19
u=9
#u=0x478dd307cdfb042d80d03e0f55227e4d982bedd1696ba700fc8ab894c504c725
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
print(" After recoring v from u through  v^2 = u^3 + Au^2 + u    : ")
print("     decimal          v = ",v)
print(" hexadecimal          v = ",hex(v))
print("     decimal    minus_v = ",minus_v)
print(" hexadecimal    minus_v = ",hex(minus_v))
print("\n")


rec_y = mont_recover_y(u,p)
print(" rec_y ",hex(rec_y))

