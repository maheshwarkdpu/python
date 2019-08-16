

from modulo_lib import *

print(" Usage:   python  euler.py  >  a ")
phi_list = [ ]
p = 61
q = 47
n = (p-1)*(q-1)
phi =0
print("p = ",p,"  = ",hex(p),"\n  q  = ",q,"   = ", hex(q))
print("n = (p-1)*(q-1) = ",hex(n)," = ",n)



for x in range(1,n):
    if(binary_gcd(x,n) == 1):
        phi = phi + 1
        phi_list.append(x)
print("phi(",hex(n),") = ",hex(phi));

print("\n")
print("------------------------------------------------")
a = euler_phi(n)
print(" euler_phi(",hex(n),")  = ",hex(a))
print("------------------------------------------------")
count=0
for x in phi_list:
    print("phi_list = ",hex(x))
    count = count+1
print("count = ",count," = ",hex(count))
print("n-count = ",n," - ", count," = ", n-count, " = ", hex(n-count))

for x in phi_list:
    for y in phi_list:
        z = x*y
        if( (z%n) == 1):
            print("x  = ",hex(x),"    x^-1 = ",hex(y)," -----",hex(x)," * ",hex(y)," = ",hex(z),"%",hex(n)," = ",hex(z%n))

print("\n")

for x in phi_list:
    print("x = ", hex(x),", phi-1  = ",hex(phi-1), ", n = ",hex(n),",  and  x ^(phi-1) mod n  = ", hex(pow(x,phi-1,n)))
print("\n\n")
#for x in phi_list:
#    print("x = ", hex(x),", phi-1  = ",hex(phi-1), ", phi = ",hex(phi),",  and  x ^(phi-1) mod phi  = ", hex(pow(x,phi-1,phi)))

print("-------- with extended eclidean(a,n)-------------")
a = 0x11
print(" a = ",hex(a),"   n = ",hex(n))
b = extended_euclidean(a,n)
print("--------------- b = ",hex(b))

print("\n\n")
print(" Usage:   python  euler.py  >  a ")
print("\n\n")



