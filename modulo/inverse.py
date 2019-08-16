

from modulo_lib import *

p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
print("p = ", hex(p))
a=0xe021757c777288dacfe67cb2e59dc02c70a8cebf56262336592c18dcf466e0a4
print("a = ", hex(a))

print("inverse(a) using Fermat a^(p-2) mod p = a^-1 ")
print("a^-1  = ",hex(pow(a,p-2,p)))


print("inverse(a) using inverse_extended_Euclidean(a,p) : ")
print("a^-1  = ",hex(binary_inverse(a,p)))


print("inverse(a) using extended_Euclidean(a,p) : ")
print("a^-1  = ",hex(extended_euclidean(a,p)))
