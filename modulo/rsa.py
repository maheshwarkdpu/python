

from modulo_lib import *


e = 65537
p = 0xfaa3bda5b5f0c65e736247b2b015cb5aeb5586dca229c680593470bdde74b843
q = 0xfa919ba26783dcd0f25681f5dd577fb29ed396dfc33a9edc5180f6c61fabfecb

print()
print("p = ",hex(p))
print()
print("q = ",hex(q))
print()
print("e = ",hex(e))
n = p*q
print("n = p*q = ",hex(n))

p_1 = p-1
q_1 = q-1
print("p-1 = ",hex(p_1))
print("q-1 = ",hex(q_1))

mul_p_1__q_1 = p_1 * q_1
print("phi = mul_p_1__q_1 = (p-1)*(q-1) = \n ", hex(mul_p_1__q_1))
phi = mul_p_1__q_1

print(" n % p  = ", hex(n%p))
print(" n % q  = ", hex(n%q))


d = 0
co_prime = gcd(e,phi)
print("gcd(e,phi) = ",co_prime)

if(co_prime == 1):
    #d = { ((k*phi(n))+1)/e }
    
    d= extended_euclidean(e,phi)
    print("d = ",hex(d))
    
    ed = (e*d)%phi 
    print("e*d mod phi = ", hex(ed))
    print("\n\n\n------------------------------------------------------------")
    print("RSA public keys  n, e ")
    print("n = p*q = ",hex(n))
    print("e = ",hex(e))
    print("\n\n\nRSA private keys  n, d ")
    print("n = p*q = ",hex(n))
    print("d = ",hex(d))
    
    print("\n\nRSA encrypt :  c  = m^e  mod n  ")
    m=0xffff00000001000000000000000000000000ffffffffffffffffffffffff
    #m=0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
    print("m = ", hex(m))
    c = pow(m,e,n)
    print("c = ", hex(c))
    
    print("\n\nRSA decrypt :  m  = c^d  mod n  ")
    m1 = pow(c,d,n)
    print("recoverd_m = ", hex(m1))
else:
    print("\n e and phi are not co-prime \n")

print("------------------------------------------------------------")
print()


