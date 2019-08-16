
import sys

def gfm(X,Y):
    R=0xe1000000000000000000000000000000
    mask=0xffffffffffffffffffffffffffffffff
    j=127
    Z=0x00000000000000000000000000000000
    V=Y
    while(j>=0):
        print(" Start loop : j=",j,)
        print(" Z = ", hex(Z))
        print(" V = ", hex(V))

        
        print(" X = ", hex(X))
        print(" j = ",j,"   X&(1<<j) = ",hex(X&(1<<j)))
        if(X&(1<<j)):
            Z = Z ^ V
            print(" Z = Z ^ V  = ", hex(Z))

        print(" (V&1) = ", (V&1))
        if(V&1):
            #V = (V >> 1)&mask
            V = (V >> 1)
            print(" (V >> 1) = ", hex(V))
            V = V & mask
            print(" (V & mask) = ", hex(V))
            V = V ^ R
            print(" V = V ^ R = ", hex(V))
        else:
            #V = (V >> 1)&mask
            V = (V >> 1)
            print(" (V >> 1) = ", hex(V))
            V = V & mask
            print(" (V & mask) = ", hex(V))

        print(" END : j=",j,)
        print(" Z = ", hex(Z))
        print(" V = ", hex(V))
        j=j-1
    return(Z)


#AES-polynomial:  x^8  + x^4  + x^3  + x  + 1
#AES-polynomial:  1 0001 1011
def aes_mul(X,Y):
    R=0x1b
    mask=0xff
    j=0
    Z=0x00
    V=X

    #print("X = ",hex(X), "  Y = ",hex(Y))
    #print("V = ",hex(V))

    while(j<8):
        #print("\n\n--------------------- Start loop : j=",j,)
        #print(" Z = ", hex(Z))
        #print(" V = ", hex(V))

        
        #print(" X = ", hex(X))
        #print(" Y = ", hex(Y))
        #print(" j = ",j,"   Y&(1<<j) = ",hex(Y&(1<<j)))
        if(Y&(1<<j)):
            Z = Z ^ V
            #print(" Z = Z ^ V  = ", hex(Z))

        #print(" (V&0x80) = ", (V&0x80))
        if(V&0x80):
            #V = (V << 1)&mask
            V = (V << 1)
            #print(" (V << 1) = ", hex(V))
            V = V ^ R
            #print(" V = V ^ R = ", hex(V))
        else:
            #V = (V << 1)&mask
            V = (V << 1)
            #print(" (V << 1) = ", hex(V))

        V = V & mask
        #print(" (V & mask) = ", hex(V))
        #print(" Z = ", hex(Z))
        #print(" V = ", hex(V))
        #print("------------------ END : j=",j,)
        j=j+1
    #print(" Z = ", hex(Z))
    return(Z)


