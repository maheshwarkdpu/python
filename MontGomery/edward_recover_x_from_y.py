

from ecc_lib import *


# Recovery x from y through RFC 8032, sec 5.1.3
# x^2 = (y^2 - 1) / (d y^2 + 1) (mod p

print("\n")
p = 2**255 - 19
d = 37095705934669439343138083508754565189542113879843219016388785533085940283555
y = 0xbfe267346819f8eb_644dfd2eef6754c3_345024e1702c93f4_3b565ead932b17ec

x_0 = (y>>31)&1
print(" x_0 = ", x_0)
mask = 2**255 - 1
y = y & mask  # clear MSB bit which is x_0
print(" y       hexadecimal   = ",hex(y))
# y^2 - 1
y2m1 = (y*y)%p - 1
# d*y^2 + 1
dy2p1 = (d*y*y) %p + 1
print(" d*y^2 + 1  : ",hex(dy2p1))
#inverse(d*y^2 + 1)
inv_dy2p1 = pow(dy2p1, p-2, p)
print(" inverse(d*y^2 + 1)  : ",hex(inv_dy2p1))
# x^2 =  { (y^2-1) * inverse(d*y^2+1) }
a = (y2m1 * inv_dy2p1)%p
print(" (y^2-1) * inverse(d*y^2 + 1)  : ",hex(a))
x = sqrt_25519(a)

print(" Recoverd y from x thtough x^2 = (y^2 - 1) / (d y^2 + 1) (mod p) : ")
print(" x       hexadecimal   = ",hex(x))
if  (x_0 ^ (x&1)):
    x = (p - x) %p
    print(" x = (p-x)      hexadecimal   = ",hex(x))
