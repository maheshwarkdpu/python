

from binary_ecc_lib import *

#AES-polynomial:  x^8  + x^4  + x^3  + x  + 1
#AES-polynomial:  1 0001 1011

#x=0x57
#y=0x83
#z = aes_mul(x,y)
#print(" z = ", hex(z))
x = [ ]
y = [ ]


i=0
while(i<256):
    j=0
    
    while(j<256):
        #print(" i = ",i,", j = ",j)
        if(aes_mul(i,j) == 1):
            print("x = ",hex(i),",  y = ",hex(j))
            x.append(i)
            y.append(j)
        j = j + 1
    i = i + 1

print(" x_list :",x)
print(" y_list :",y)

i=0
while(i<255):
    #print(" x * y = aes_mul(x,y) = ")
    print("i = ",i,"  ",hex(x[i]) ," * ", hex(y[i]) ," = ", aes_mul(x[i],y[i]))
    i = i + 1
print("\n")
