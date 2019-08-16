#! /usr/bin/python



import sys

from ecc_lib import *

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

double=0
add=0
upm=0
fpm=0

lineno = 0

x1=y1=z1=x2=y2=z2=0
scalar=0
rx=ry=rz=0
Gz=1

prime_length=0
window=4
table=0
print("\n\n Usage: python3.7  fecc.py < NIST_p256.txt \n\n")
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

    #ECC operation Selection 
    if(line[0:3] == "DBL"):
        double=1; add=0; upm=0; fpm=0; continue
    elif(line[0:3] == "ADD"):
        double=0; add=1; upm=0; fpm=0; continue
    elif(line[0:3] == "UPM"):
        double=0; add=0; upm=1; fpm=0; continue
    elif(line[0:3] == "FPM"):
        double=0; add=0; upm=0; fpm=1; continue

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
    #print(" double=",double," add=",add," upm=",upm," fpm=",fpm)


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


    #print(" ----------------------------------------------")
    if(double == 1):
        #print(" ----------------------------------------------")
        if(line[0:3] == "x1="):
            x1 = int(line[3:],16)
            print("\nDBL inputs:-------------------------------------------\nx1=",hex(x1))
            continue
        if(line[0:3] == "y1="):
            y1 = int(line[3:],16)
            print("y1=",hex(y1))
            continue
        if(line[0:3] == "z1="):
            z1 = int(line[3:],16)
            print("z1=",hex(z1))

        rx,ry,rz = ecc_double(x1,y1,z1,a,p)
        #print("after ecc_double : X,Y,Z")
        #print(" x = ", hex(rx))
        #print(" y = ", hex(ry))
        #print(" z = ", hex(rz))
        inv_rz = pow(rz,(p-2),p)
        rx = (rx * inv_rz)%p
        ry = (ry * inv_rz)%p
        print(" DBL result :")
        print(" x = ", hex(rx))
        print(" y = ", hex(ry))
        #print(" z = ", hex((rz*inv_rz) % p))
        print(" ================================================")

    elif(add == 1):
        #print(" ----------------------------------------------")
        if(line[0:3] == "x1="):
            x1 = int(line[3:],16)
            print("\nADD inputs:-------------------------------------------\nx1=",hex(x1))
            continue
        if(line[0:3] == "y1="):
            y1 = int(line[3:],16)
            print("y1=",hex(y1))
            continue
        if(line[0:3] == "z1="):
            z1 = int(line[3:],16)
            print("z1=",hex(z1))
            continue

        if(line[0:3] == "x2="):
            x2 = int(line[3:],16)
            print("x2=",hex(x2))
            continue
        if(line[0:3] == "y2="):
            y2 = int(line[3:],16)
            print("y2=",hex(y2))
            continue
        if(line[0:3] == "z2="):
            z2 = int(line[3:],16)
            print("z2=",hex(z2))

        rx,ry,rz = ecc_add(x1,y1,z1,x2,y2,z2,a,p)
        #print("after ecc_add : X,Y,Z")
        #print(" x = ", hex(rx))
        #print(" y = ", hex(ry))
        #print(" z = ", hex(rz))
        inv_rz = pow(rz,(p-2),p)
        rx = (rx * inv_rz)%p
        ry = (ry * inv_rz)%p
        print(" ADD result :")
        print(" x = ", hex(rx))
        print(" y = ", hex(ry))
        #print(" z = ", hex((rz*inv_rz) % p))
        print(" ================================================")

    elif(upm == 1):
        #print(" ----------------------------------------------")
        if(line[0:3] == "x1="):
            x1 = int(line[3:],16)
            print("\nUPM inputs:-------------------------------------------\nx1=",hex(x1))
            continue
        if(line[0:3] == "y1="):
            y1 = int(line[3:],16)
            print("y1=",hex(y1))
            continue
        if(line[0:3] == "z1="):
            z1 = int(line[3:],16)
            print("z1=",hex(z1))
            continue
        if(line[0:7] == "scalar="):
            scalar = int(line[7:],16)
            print("scalar=",hex(scalar))

        rx,ry,rz = ecc_mul(x1,y1,z1,scalar,a,p)
        #print("after ecc_mul_upm : X,Y,Z")
        #print(" x = ", hex(rx))
        #print(" y = ", hex(ry))
        #print(" z = ", hex(rz))
        inv_rz = pow(rz,(p-2),p)
        rx = (rx * inv_rz)%p
        ry = (ry * inv_rz)%p
        print(" UPM result :")
        print(" x = ", hex(rx))
        print(" y = ", hex(ry))
        #print(" z = ", hex((rz*inv_rz) % p))
        print(" ================================================")

    elif(fpm == 1):
        #print(" ----------------------------------------------")
        if(line[0:3] == "x1="):
            x1 = int(line[3:],16)
            print("\nFPM inputs:-------------------------------------------\nx1=",hex(x1))
            continue
        if(line[0:3] == "y1="):
            y1 = int(line[3:],16)
            print("y1=",hex(y1))
            continue
        if(line[0:3] == "z1="):
            z1 = int(line[3:],16)
            print("z1=",hex(z1))
            continue
        if(line[0:7] == "scalar="):
            scalar = int(line[7:],16)
            print("scalar=",hex(scalar))

        table = fpm_table(Gx,Gy,Gz,a,p,prime_length,window)
        rx,ry,rz = ecc_mul_fpm(table,scalar,a,p,prime_length,window)
        print("after ecc_mul_fpm : X,Y,Z")
        print(" x = ", hex(rx))
        print(" y = ", hex(ry))
        print(" z = ", hex(rz))
        inv_rz = pow(rz,(p-2),p)
        rx = (rx * inv_rz)%p
        ry = (ry * inv_rz)%p
        print(" FPM result :")
        print(" window=",window)
        print(" x = ", hex(rx))
        print(" y = ", hex(ry))
        #print(" z = ", hex((rz*inv_rz) % p))
        print(" ================================================")
print()




