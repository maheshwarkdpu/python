

from modulo_lib import *


e = 65537

#p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
#q = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

p = 0xfaa3bda5b5f0c65e736247b2b015cb5aeb5586dca229c680593470bdde74b843
q = 0xfa919ba26783dcd0f25681f5dd577fb29ed396dfc33a9edc5180f6c61fabfecb

#p=0xf4f679b90b986d2a2e83c61af3f3f86016104c11c8e16aa26a52f13123c72671
#q=0xee2ecb7c3b9bfbdd3f1e13c850c3b1309fa78203d379e72a2e0abe3c3288d1a3
#expected d=0x10bc00472985740cd5c601566a61e3d64413e681f32f33103d926df683057566f2e6b6a0c60baf7cde52e96b1dc648ff303fa261eaa5535843089b42f5e20a81

#e=17
#p=61 #151 #643 #401  #61
#q=47 #149 #641 #397  #53
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
e_phi = mul_p_1__q_1 // gcd_p_1__q_1
print("e_phi = lcm(p-1,q-1) = ((p-1)*(q-1))/gcd(p-1,q-1) = \n ",hex((e_phi)))


d = 0
co_prime = gcd(e,e_phi)
print("gcd(e,e_phi) = ",co_prime)

if(co_prime == 1):
    #d = { ((k*phi(n))+1)/e }
    d= extended_euclidean(e,mul_p_1__q_1)
    print("d = ",hex(d))
    
    print("e = ",hex(e))
    ed = (e*d)%mul_p_1__q_1
    print("e*d mod mul_p_1__q_1 = ", hex(ed))
    
    m=0xffff00000001000000000000000000000000ffffffffffffffffffffffff
    #m=0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
    print("m = ", hex(m))
    c = pow(m,e,n)
    print("c = ", hex(c))
    
    m1 = pow(c,d,n)
    print("recoverd_m = ", hex(m1))
else:
    print("\n e and phi are not co-prime \n")





########### CRT

print("\n\n ----------------------------CRT------------------------ \n")
dp =  d % p_1
dq =  d % q_1
qInv = pow(q, p-2, p)
print(" dP = ", hex(dp))
print(" dQ = ", hex(dq))
print(" iqmp = ",hex(qInv))

edP  = (e*dp)%(p-1)
edQ  = (e*dq)%(q-1)
print("edP = e*dP mod (p-1) = ",edP,"\nedQ = e*dQ mod (q-1) = ",edQ)

m1 = pow(c,dp,p)
print("m1 = ",hex(m1))
m2 = pow(c,dq,q)
print("m2 = ",hex(m2))
h = (qInv * (m1 - m2))%p
print("h = ",hex(h))
m3 = (m2 + (h*q))
print("recoverd_m = ", hex(m3))




