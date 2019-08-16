#! /usr/bin/python3.6
import sys
from ecc_lib import *

#http://samuelkerr.com/?p=431

##constants
#Gx = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
#Gy = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
#Gz = 0x1
#order = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
#a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
#p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff

#montgomery constants in Weierstrass form
p =  0x7fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffed
a =  0x2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa984914a144
b =  0x7b425ed097b425ed097b425ed097b425ed097b425ed097b4260b5e9c7710c864
order = 2**252 + 0x14def9dea2f79cd65812631a5cf5d3ed
Gx = 0x2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad245a
Gy = 0x20ae19a1b8a086b4e01edd2c7748d14c923d4d7e6d7c61b229e9c5a27eced3d9
Gz = 0x1



def gen_ecc_mul(x1, y1, z1, scalar):
    x2, y2, z2 = ecc_mul(x1, y1, z1, scalar, a, p)
    return(x2, y2, z2)




def gen_ecc_add(x1,y1,z1,x2,y2,z2):
    rx,ry,rz = ecc_add(x1,y1,z1,x2,y2,z2,a,p)
    return(rx, ry, rz)


debug = 1


K = 0x0000000000000000000000000000000000000000000000000000000000000002
D = 0x0000000000000000000000000000000000000000000000000000000000000001
E = 0x0000000000000000000000000000000000000000000000000000000000000001



print("--------------ECDSA--Sign-------------------")
# 1.Calculate e={HASH}(m).
# 2.Let z be the L_{n} leftmost bits of e, where L_{n} is the bit length of the group order n.
# 3.Select a cryptographically secure random integer k from [1,n-1].
# 4.Calculate the curve point (x1,y1) = k *  G.
# 5.Calculate r=x1 mod n. If r=0, go back to step 3.
# 6.Calculate s= inv(k) (z + rd) n. If s=0, go back to step 3.
# 7.The signature is the pair (r,s).

K = order
if(debug):
    print(" before k * G(x,y) ")
    print(" X = ", hex(Gx))
    print(" Y = ", hex(Gy))
    print(" Z = ", hex(Gz))
    print(" k = ", hex(K))
rx,ry,rz = gen_ecc_mul(Gx,Gy,Gz,K)
if(0):
    print("after k * G(x,y) ")
    print(" X = ", hex(rx))
    print(" Y = ", hex(ry))
    print(" Z = ", hex(rz))
inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
ry = (ry * inv_rz)%p

if(debug):
    print("\nafter k * G(x,y) ")
    print(" x = ", hex(rx))
    print(" y = ", hex(ry))

R = rx
# Inverse(K)
inv_k = pow(K, (order-2), order)
rd = (R * D)%order
zprd = (E + rd)%order
S = (inv_k * zprd)%order

if(debug):
    print(" R = ", hex(R))
    print(" S = ", hex(S))




#Generate public key Q = D * G

rx,ry,rz = gen_ecc_mul(Gx,Gy,Gz,D)
if(debug):
    print(" after k * G(x,y) ")
    print(" X = ", hex(rx))
    print(" Y = ", hex(ry))
    print(" Z = ", hex(rz))
inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
ry = (ry * inv_rz)%p
Qx = rx
Qy = ry
Qz = (rz * inv_rz)%p
if(debug):
    print(" Qx = ", hex(Qx))
    print(" Qy = ", hex(Qy))
    print(" Qz = ", hex(Qz))



print("--------------ECDSA--Verify-------------------")
# 1. Calculate e={HASH}(m).
# 2. Let z be the L_{n} leftmost bits of e, where L_{n} is the bit length of the group order n.
# 3. Calculate u1 = z * inv(s), u2 = r * inv(s) mod n.
# 4. Calculate (x1, y1) = u1 * G(x,y) + u2 * Q(x,y).
# 5. Signature is valid if x1 == r, else invalid.


#w = Inverse(S)
w = pow(S,(order-2),order)
if(debug):
    print(" w = Inverse(S) ", hex(w))

#u1 = z * w
u1 = (E * w)%order
if(debug):
    print(" u1 = z * w ", hex(u1))

# u2 = R * w
u2 = (R * w)%order
if(debug):
    print(" u2 = rw ", hex(u2))

# u1 * G(x,y)
rx,ry,rz = gen_ecc_mul(Gx,Gy,Gz,u1)
if(debug):
    print(" after u1 * G(x,y) ")
    print(" X = ", hex(rx))
    print(" Y = ", hex(ry))
    print(" Z = ", hex(rz))
inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
ry = (ry * inv_rz)%p
rz = (rz * inv_rz)%p
if(debug):
    print(" x = ", hex(rx))
    print(" y = ", hex(ry))
    print(" z = ", hex(rz))
    print()

# u2 * Q(x,y)
sx,sy,sz = gen_ecc_mul(Qx,Qy,Qz,u2)
if(debug):
    print(" after u2 * Q(x,y) ")
    print(" X = ", hex(sx))
    print(" Y = ", hex(sy))
    print(" Z = ", hex(sz))
inv_sz = pow(sz,(p-2),p)
sx = (sx * inv_sz)%p
sy = (sy * inv_sz)%p
sz = (sz * inv_sz)%p
if(debug):
    print(" x = ", hex(sx))
    print(" y = ", hex(sy))
    print(" z = ", hex(sz))
    print()

#  (u1*G(x,y)  + u2*Q(x,y) 
if(debug):
    print(" Point-Add inputs : ")
    print(" RX = ", hex(rx))
    print(" RY = ", hex(ry))
    print(" RZ = ", hex(rz))
    print(" SX = ", hex(sx))
    print(" SY = ", hex(sy))
    print(" SZ = ", hex(sz))
rx,ry,rz = gen_ecc_add(rx,ry,rz,sx,sy,sz)
if(debug):
    print(" after (u1 * G(x,y)   +   u2*Q(x,y)  ")
    print(" X = ", hex(rx))
    print(" Y = ", hex(ry))
    print(" Z = ", hex(rz))
inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
ry = (ry * inv_rz)%p
if(debug):
    print(" x = ", hex(rx))
    print(" y = ", hex(ry))
    print()

if(rx == R):
    print(" Ecdsa Sign/Verify PASSED")
    if(debug):
        print(" rx : ", hex(rx))
        print(" R : ", hex(R))
else:
    print(" Ecdsa Sign/Verify FAILED ")
    if(debug):
        print(" rx : ", hex(rx))
        print(" R : ", hex(R))


