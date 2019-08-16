#! /usr/bin/python



import sys

from ecc_lib import *

debug = 0

nist=0
secp=0
brainpool=0
frp=0

p160=0
p192=0
p224=0
p256=0
p320=0
p384=0
p512=0
p521=0

count=0
lineno = 0

x1=y1=z1=x2=y2=z2=0
scalar=0
rx=ry=rz=0
Gz=1

prime_length=0
window=4
table=0

K=0
D=0
E=0


print("\n\n Usage: python3.7  ecdsa.py < ecdsa_NIST_p256.txt \n\n")
while True:
    line = sys.stdin.readline()
    if not line:
        break
    lineno = lineno + 1
    if(line[0] == " "):
        continue

    if(line[0] == "\n"):
        continue

    if(line[0] == "#"):
        continue

    #print(lineno)
    #print(line)

    #Curve Type Selection 
    if(line[0:4] == "NIST"):
        nist=1; secp=0; brainpool=0; frp=0; continue
    elif(line[0:4] == "SECP"):
        nist=0; secp=1; brainpool=0; frp=0; continue
    elif(line[0:9] == "Brainpool"):
        nist=0; secp=0; brainpool=1; frp=0; continue
    elif(line[0:3] == "FRP"):
        nist=0; secp=0; brainpool=0; frp=1; continue


    #PrimeCurve Type Selection 
    if(line[0:4] == "P256"):
        p160=0; p192=0; p224=0; p256=1; p320=0; p384=0; p512=0; p521=0; continue
    elif(line[0:4] == "P320"):
        p160=0; p192=0; p224=0; p256=0; p320=1; p384=0; p512=0; p521=0; continue
    elif(line[0:4] == "P384"):
        p160=0; p192=0; p224=0; p256=0; p320=0; p384=1; p512=0; p521=0; continue
    elif(line[0:4] == "P512"):
        p160=0; p192=0; p224=0; p256=0; p320=0; p384=0; p512=1; p521=0; continue
    elif(line[0:4] == "P521"):
        p160=0; p192=0; p224=0; p256=0; p320=0; p384=0; p512=0; p521=1; continue
    elif(line[0:4] == "P224"):
        p160=0; p192=0; p224=1; p256=0; p320=0; p384=0; p512=0; p521=0; continue
    elif(line[0:4] == "P192"):
        p160=0; p192=1; p224=0; p256=0; p320=0; p384=0; p512=0; p521=0; continue
    elif(line[0:4] == "P160"):
        p160=1; p192=0; p224=0; p256=0; p320=0; p384=0; p512=0; p521=0; continue


    # Prime Length selection
    if  (p160 == 1):  prime_length=20
    elif(p192 == 1):  prime_length=24
    elif(p224 == 1):  prime_length=28
    elif(p256 == 1):  prime_length=32
    elif(p320 == 1):  prime_length=40
    elif(p384 == 1):  prime_length=48
    elif(p512 == 1):  prime_length=64
    elif(p521 == 1):  prime_length=66

    #print(" nist=", nist, " secp=",secp," brainpool=",brainpool," frp=",frp)
    #print(" p160=",p160," p192=",p192," p224=",p224," p256=",p256," p320=",p320," p384=",p384," p512=",p512," p521=",p521)


    if(line[0:6] == "Prime="):
        p = int(line[6:],16)
        print(" Prime: ",hex(p))
        continue

    if(line[0:6] == "Order="):
        order = int(line[6:],16)
        print(" Order: ",hex(order))
        continue

    if(line[0:2] == "A="):
        a = int(line[2:],16)
        print(" A: ",hex(a))
        continue

    if(line[0:2] == "B="):
        b = int(line[2:],16)
        print(" B: ",hex(b))
        continue

    if(line[0:3] == "Gx="):
        Gx = int(line[3:],16)
        print(" Gx: ",hex(Gx))
        continue

    if(line[0:3] == "Gy="):
        Gy = int(line[3:],16)
        print(" Gy: ",hex(Gy))
        continue

    if(line[0:6] == "COUNT="):
        count = int(line[6:],10)
        print(" \ncount = : ",count)
        continue

    if(line[0:2] == "K="):
        K = int(line[2:],16)
        print(" K  : ",hex(K))
        continue

    if(line[0:2] == "D="):
        D = int(line[2:],16)
        print(" D  : ",hex(D))
        continue

    if(line[0:2] == "E="):
        E = int(line[2:],16)
        print(" E  : ",hex(E))


    if(debug):
        print("--------------ECDSA--Sign-------------------")
    #  k * G(x,y)
    #rx,ry,rz = ecc_mul(Gx,Gy,Gz,K,a,p)
    table = fpm_table(Gx,Gy,Gz,a,p,prime_length,window)
    rx,ry,rz = ecc_mul_fpm(table,K,a,p,prime_length,window)
    if(debug):
        print(" after k * G(x,y) ")
        print(" X = ", hex(rx))
        print(" Y = ", hex(ry))
        print(" Z = ", hex(rz))
    inv_rz = pow(rz,(p-2),p)
    rx = (rx * inv_rz)%p
    ry = (ry * inv_rz)%p
    if(debug):
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

        print("--------------ECDSA--Verify-------------------")
    #rx,ry,rz = ecc_mul(Gx,Gy,Gz,D,a,p)
    rx,ry,rz = ecc_mul_fpm(table,D,a,p,prime_length,window)
    if(debug):
        print(" after d * G(x,y) ")
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

    # w = Inverse(S)
    w = pow(S,(order-2),order)
    if(debug):
        print(" w = Inverse(S) ", hex(w))

    # u1 = Ew
    u1 = (E * w)%order
    if(debug):
        print(" u1 = ew ", hex(u1))

    # u2 = Rw
    u2 = (R * w)%order
    if(debug):
        print(" u2 = rw ", hex(u2))

    # u1 * G(x,y)
    #rx,ry,rz = ecc_mul(Gx,Gy,Gz,u1,a,p)
    rx,ry,rz = ecc_mul_fpm(table,u1,a,p,prime_length,window)
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
    sx,sy,sz = ecc_mul(Qx,Qy,Qz,u2,a,p)
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
    rx,ry,rz = ecc_add(rx,ry,rz,sx,sy,sz,a,p)
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
print()




