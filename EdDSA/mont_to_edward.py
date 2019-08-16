


# Montgomery (u,v) coordinates to Edwarad (x,y) coordinate converstion.
# (x, y) = (sqrt(-486664)*u/v, (u-1)/(u+1))

# from RFC-8032, Sec. 5.1.1
def sqrt_25519(a):
    #print("\n ---------------------------------------")
    minus_a = -a % p
    #print("\n a : ", (a))
    #print("\n a : ", hex(a))
    #print("\n minus_a : ", (minus_a))
    #print("\n minus_a : ", hex(minus_a))
    x = pow(a, (p+3)//8, p)
    #print("\n x : ", (x))
    #print("\n x : ", hex(x))
    x2 = (x*x) % p
    #print("\n x2 : ", (x2))
    #print("\n x2 : ", hex(x2))
    #print("\n type(x2)  = ", type(x2))
    #print("\n type(a)  = ", type(a))
    if  x2 == a:
        #print("\n x2 == a")
        sqrt_x = x
    elif x2 == minus_a:
        #print("\n x2 == minus_a")
        sqrt_x = (pow(2,(p-1)//4,p)*x)%p

    #print("\n sqrt_x : ", (sqrt_x))
    #print("\n sqrt_x : ", hex(sqrt_x))
    #print("\n ---------------------------------------")
    return sqrt_x


def printx(val):
    print("\n val : ", hex(val))

p = 2**255  - 19
u = 9
v = 14781619447589544791020593568409986887264606134616475288964881837755586237401
print("\n MOntgomery 25519  Base points ")
print(" u  decimal : ", u)
print(" u      hex : ", hex(u))
print(" v  decimal : ", v)
print(" v      hex : ", hex(v))
print("\n\n After Converting from Montgomery(u,v) to Edward (x,y) co-ordinates : ")

A = 486664
minus_A = -A
#print ("\n minus_A : ", minus_A)
#print ("\n minus_A hex : ", hex(minus_A))
minus_A = minus_A % p
#print ("\n minus_A : ", minus_A)
#print ("\n minus_A hex : ", hex(minus_A))
sqrt_A  = sqrt_25519(minus_A)
#print("\n sqrt_A : ",hex(sqrt_A))
inverse_v = pow(v, (p-2), p)

#print("\n inverse_v : ", hex(inverse_v))
x = (sqrt_A * u * inverse_v) % p

minus_x = -x
minus_x = minus_x % p


um1 = u-1
up1 = u+1

inverse_up1  =  pow(up1, (p-2), p)

y = (um1 * inverse_up1) % p


#print(" x           decimal   = ",x)
#print(" x       hexadecimal   = ",hex(x))
print(" minus_x     decimal   = ",minus_x)
print(" minus_x hexadecimal   = ",hex(minus_x))
print(" y           decimal   = ",y)
print(" y       hexadecimal   = ",hex(y))


print("\n Edward 25519  Base points ")
x = 15112221349535400772501151409588531511454012693041857206046113283949847762202
y = 46316835694926478169428394003475163141307993866256225615783033603165251855960

print(" x  decimal : ", x)
print(" x      hex : ", hex(x))
print(" y  decimal : ", y)
print(" y      hex : ", hex(y))


