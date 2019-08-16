

from modulo_lib import *


e = 65537
p = 0xfaa3bda5b5f0c65e736247b2b015cb5aeb5586dca229c680593470bdde74b843
q = 0xfa919ba26783dcd0f25681f5dd577fb29ed396dfc33a9edc5180f6c61fabfecb


#p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
#q = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

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
print("mul_p_1__q_1 = (p-1)*(q-1) = \n ", hex(mul_p_1__q_1))
gcd_p_1__q_1 = binary_gcd(p_1,q_1)
print("gcd_p_1__q_1 = gcd(p-1,q-1) = ",hex(gcd_p_1__q_1))
euler_phi = mul_p_1__q_1
print("euler_phi = ((p-1)*(q-1)) = \n ",hex((euler_phi)))
gamma = mul_p_1__q_1 // gcd_p_1__q_1
print("gamma = lcm(p-1,q-1) = ((p-1)*(q-1))/gcd(p-1,q-1) = \n ",hex((gamma)))


d = 0
co_prime1 = gcd(e,euler_phi)
print("gcd(e,euler_phi) = ",co_prime1)
co_prime2 = gcd(e,gamma)
print("gcd(e,gamma) = ",co_prime2)

if((co_prime1 == 1) and (co_prime2 == 1)):
    #d = { ((k*phi(n))+1)/e }
    print("\n----------------using Euler_phi(n)--------------------")
    d= extended_euclidean(e,euler_phi)
    print("d = ",hex(d))
    
    print("e = ",hex(e))
    ed = (e*d)%euler_phi 
    print("e*d mod euler_phi = ", hex(ed))
    
    m=0xffff00000001000000000000000000000000ffffffffffffffffffffffff
    print("m = ", hex(m))
    c = pow(m,e,n)
    print("c = ", hex(c))
    
    m1 = pow(c,d,n)
    print("recoverd_m = ", hex(m1))



    #d = { ((k*phi(n))+1)/e }
    print("\n----------------using Gamma(n)--------------------")
    d= extended_euclidean(e,gamma)
    print("d = ",hex(d))
    
    print("e = ",hex(e))
    ed = (e*d)%gamma
    print("e*d mod gamma = ", hex(ed))
    
    m=0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
    print("m = ", hex(m))
    c = pow(m,e,n)
    print("c = ", hex(c))
    
    m1 = pow(c,d,n)
    print("recoverd_m = ", hex(m1))



else:
    print("\n e and phi are not co-prime \n")

print()


