


# y^2  =  x^3  + 486662*x^2   +   x
# 
# y    =  sqrt(x^3  + 486662*x^2   +   x)
#
#   To find a square root of a, first compute the candidate root
#      x = a^((p+3)/8) (mod p).  Then there are three cases:
#
#      x^2 = a (mod p).  Then x is a square root.
#
#      x^2 = -a (mod p).  Then 2^((p-1)/4) * x is a square root.
#
#      a is not a square modulo p.
#
def sqrt_25519(a):
    minus_a = -a % p
    x = pow(a, (p+3)//8, p)
    x2 = (x*x) % p
    if  x2 == a:
        sqrt_x = x
    elif x2 == minus_a:
        sqrt_x = (pow(2,(p-1)//4,p)*x)%p

    return sqrt_x



p = 2**255  - 19
print("\n prime : ", hex(p))
x=9
print("\n")
print(" x =       ", x)
x3 = (x*x*x)%p
Ax2 = (486662*x*x)%p
x_result = (x3 + Ax2 + x)%p
#x2 = pow(x_result, (p+3)//8, p)
#x2 = (x2*x2) % p
a = x_result
minus_a =  -a
minus_a = minus_a % p
sqrt_x  = sqrt_25519(a)
#x = pow(a, (p+3)//8, p)
#x2 = (x*x) % p
#
#print("\n y = \n")
#if  x2 == a:
#    print("\n \t\t decimal = ", x)
#    print("\n \t\t hex = ", hex(x))
#elif x2 == minus_a:
#    sqrt_x = (pow(2,(p-1)//4,p)*x)%p
#    print("\n \t\t decimal = ", sqrt_x)
#    print("\n \t\t hex = ", hex(sqrt_x))
#
print("\n y = ")
print(" decimal = ", sqrt_x)
print(" hex =     ", hex(sqrt_x))
print("\n")

