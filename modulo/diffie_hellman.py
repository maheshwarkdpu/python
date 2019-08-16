

# Diffi-Hellman Key Exchange

# choose prime, p
print()
p=0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
print("prime = \n",hex(p))

# choose generator, g
print("Choosen Generator, g = ")
g=0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604d
print(hex(g))

print()
# How to check whether g is generator or not.   
# g^((p-1)/2) mod p  ====>>  p-1   
if(pow(g,(p-1)>>1,p) == (p-1)):
    print(" yes choosen G  is generator = ") 
else:
    print(" yes choosen G is not generator = ") 


print("\n\n")
# Alice secret key, a
print("Alice secret key, a : ")
a=0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296 
print(hex(a))


print("\n\n")
# Bob secret key, b
print("Bob secret key, b : ")
b=0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
print(hex(b))



print("\n\n")
# Alice public key, aa = g^a mod p
print("Alice public key, aa = g^a mod p : ")
aa =  pow(g,a,p)
print(hex(aa))



print("\n\n")
# Bobs public key, bb = g^b mod p
print("Bobs public key, bb = g^b mod p : ")
bb = pow(g,b,p)
print(hex(bb))


print("\n\n")
# Exchange their public keys each other
print("---------Exchange their public keys each other------")


print("\n\n")
# Alice Shared Secret = bb^a mod p
print("Alice Shared Secret = bb^a mod p : ")
a_ss = pow(bb,a,p)
print(hex(a_ss))


print("\n\n")
# Bobs Shared Secret = aa^b mod p
print("Bobs Shared Secret = aa^b  mod p : ")
b_ss = pow(aa,b,p)
print(hex(b_ss))


print("\n\n")
# Both Shared Secrets are same 
print("Both Shared Secrets are same  ")
print("\n\n")



