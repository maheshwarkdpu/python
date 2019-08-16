

from modulo_lib import *


e = 65537

#p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
#q = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

p = [ 0xfaa3bda5b5f0c65e736247b2b015cb5aeb5586dca229c680593470bdde74b843,
      0xfa919ba26783dcd0f25681f5dd577fb29ed396dfc33a9edc5180f6c61fabfecb,
      0xA9FB57DBA1EEA9BC3E660A909D838D718C397AA3B561A6F7901E0E82974856A7]

d = [ ]
t = [ ]

#p=0xf4f679b90b986d2a2e83c61af3f3f86016104c11c8e16aa26a52f13123c72671
#q=0xee2ecb7c3b9bfbdd3f1e13c850c3b1309fa78203d379e72a2e0abe3c3288d1a3
#expected d=0x10bc00472985740cd5c601566a61e3d64413e681f32f33103d926df683057566f2e6b6a0c60baf7cde52e96b1dc648ff303fa261eaa5535843089b42f5e20a81

n=1
euler_phi=1
print()
for i in range(0,3):
    print("p[",i,"] = ",hex(p[i]))
    print("p[",i,"]  - 1  = ",hex(p[i]-1))
    n = n*p[i]
    euler_phi = euler_phi * (p[i]-1)
    print()



print("e = ",hex(e))
print("n = p*q*r = ",hex(n))
print("euler_phi = (p-1)*(q-1)*(r-1)  = \n",hex(euler_phi))


print()
print("gcd(e,euler_phi) = ", binary_gcd(e,euler_phi))

for i in range(0,3):
    temp_d = extended_euclidean(e,p[i]-1)
    d.append(temp_d)
    print(" d[",i,"] =  ", hex(d[i]))
    print(" e*temp_d mod (p(i)-1) = ", (e*temp_d)%(p[i]-1))


for i in range(0,3):
    print("n = p*q*r = ",hex(n))
    print(" n % (p(i))  = ",n%(p[i]))

    temp_t = extended_euclidean(n,p[i])
    #temp_t = extended_euclidean(n%(p[i]),p[i])
    print("temp_t = ", hex(temp_t))
    print(" n* temp_t mod (p(i))  = ", (n*temp_t)%(p[i]))

exit(0)

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




