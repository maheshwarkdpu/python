#Python Program to find the L.C.M. of two input number

debug=0
# define a function
def lcm(x, y):
#    greater = 0
#    """This function takes two
#    integers and returns the L.C.M."""
#
#    # choose the greater number
#    if x > y:
#        greater = x
#    else:
#        greater = y
#
#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1
#
#    return lcm

    z = gcd(x,y)
    lcm = (x*y)//z
    return(lcm)

def gcd(a,b):
    if(debug == 1):
        print("------------------- gcd start ----------------------- ")
        print("a = ", hex(a))
        print("b = ", hex(b))
    x = b%a
    if(debug == 1):
        print("x = ", hex(x))
    while(x != 0):
        b = a
        a = x
        x = b%a
        if(debug == 1):
            print("x = ", hex(x))
            print("a = ", hex(a))
    if(debug == 1):
        print("------------------- gcd end ----------------------- ")
    return(a)


def binary_gcd(a,b):
    u = a
    v = b
    e = 1
    while(((u&1)==0) and ((v&1)==0)):
            u = u >> 1
            v = v >> 1
            e = e << 1

    while(u!=0):
        while((u&1)==0):
            u = u >> 1
        while((v&1)==0):
            v = v >> 1
        if(u>=v):
            u = u - v
        else:
            v = v - u

    return(e*v)

    



def binary_inverse(a,p):
    #invsere in Fp using Extended Euclidean algorithm
    u = a
    v = p
    x1 = 1
    x2 = 0
    while((u != 1) and (v != 1)):
        while((u&1) == 0):
            u = u >> 1
            if((x1&1) == 0):
                x1 = x1 >> 1
            else:
                x1 = (x1+p) >> 1

        while((v&1) == 0):
            v = v >> 1
            if((x2&1) == 0):
                x2 = x2 >> 1
            else:
                x2 = (x2+p) >> 1

        if(u>=v):
            u = u - v
            x1 = x1 - x2
        else:
            v = v - u
            x2 = x2 - x1

    if(u == 1):
        return(x1%p)
    else:
        return(x2%p)




def euler_phi(n):
    result = n
    i = 2
    while((i*i)<=n):
        if((n%i) == 0):
            while((n%i)==0):
                #print(" n = ", hex(n),", i = ",hex(i))
                n = n // i
                #print(" n = ", hex(n))
            result = result - (result // i)
            #print(" result = ", hex(result))
        i = i + 1
    if(n>1):
        result = result - (result // n)
    return(result)





#function inverse(a, n)
#    t := 0;     newt := 1;    
#    r := n;     newr := a;    
#    while newr ≠ 0
#        quotient := r div newr
#        (t, newt) := (newt, t - quotient * newt) 
#        (r, newr) := (newr, r - quotient * newr)
#    if r > 1 then return "a is not invertible"
#    if t < 0 then t := t + n
#    return t



def extended_euclidean(a, n):
    t = 0;     newt = 1;
    r = n;     newr = a;
    while (newr !=  0):
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)
    if (r > 1): 
        print( "a is not invertible")
        exit()
    if (t < 0):
        t = t + n
    return t




