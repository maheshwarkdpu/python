





#/*
# **  Syntax:
# **    curve25519_ladder_step()
# ** 
# **  Description:
# **
# **  (Initially only)
# **  X1 <------  1
# **  Z1 <------  0
# **  X2 <------  xP (original x-coordinate)
# **  Z2 <------  1
# **
# **    This subroutine does the ladderstep of curve25519 of a point (X1,Z1) 
# **    and (X2,Z2) with xP(original x-coordinate)
# **    The resulting (X1, Z1) has Double Result and  (X2, Z2) has Add Result.
# **    
# **  Inputs:
# **    X1,Z1,X2,Z2 and xP(original x-coordinate) 
# **    PRIME 2^255  - 19  
# **     
# **  Output:
# **    X1,Z1,X2,Z2   i.e (X1,Z1) has Double Result,  (X2,Z2) has Add Result. 
# **   
# **  Registers Modified:
# **    All
# ** 
# **  Implementation Algorithm: 
#     Ladder Step: http://cr.yp.to/ecdh/curve25519-20060209.pdf
#
 	
def x25519_ladder_step(X1,Z1,X2,Z2,xP,A24,p):
    T1 = (X2  +  Z2  )%p  
    X2 = (X2  -  Z2  )%p  
    Z2 = (X1  +  Z1  )%p  
    X1 = (X1  -  Z1  )%p  
    T1 = (T1  *  X1  )%p  
    X2 = (X2  *  Z2  )%p  
    Z2 = (Z2  *  Z2  )%p  
    X1 = (X1  *  X1  )%p  
    T2 = (Z2  -  X1  )%p  
    Z1 = (T2  *  A24 )%p   
    Z1 = (Z1  +  X1  )%p  
    Z1 = (T2  *  Z1  )%p  
    X1 = (Z2  *  X1  )%p  
    Z2 = (T1  -  X2  )%p  
    Z2 = (Z2  *  Z2  )%p  
    Z2 = (Z2  *  xP  )%p  
    X2 = (T1  +  X2  )%p  
    X2 = (X2  *  X2  )%p  
    return(X1,Z1,X2,Z2)


def cswap(a,b,c):
    #tmp <---- X1
    #X1  <---- X2
    #X2  <---- tmp
    #print(" c = ", c)
    if(c == 1):
        #print(" inside c = ", c)
        tmp = a
        a = b
        b = tmp
    return(a,b)



def ecc_mul_x25519(x1,scalar, A24, p):
    # mask scalar
    # clear 255-th bit, and set 254-th bit
    #print(" b4 mask scalar : ",hex(scalar))
    mask1 = 0x4000000000000000000000000000000000000000000000000000000000000000
    mask2 = 0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8
    scalar = scalar | mask1
    scalar = scalar & mask2
    print(" after mask scalar : ",hex(scalar))
    X1 = 1
    Z1 = 0
    X2 = x1
    Z2 = 1
    pp = 0
    i = 254
    while (i>=0):
        b = ((scalar>>i)&1)
        c = b ^ pp
        print(" scalar>>",i,"&1, ---------b = ",b,"     c= ",c, "   pp=",pp);
        pp = b
        X1,X2 = cswap(X1,X2,c)
        Z1,Z2 = cswap(Z1,Z2,c)
        print(" Before Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        print(" xP : ",hex(x1))
        print(" X1 : ",hex(X1))
        print(" Z1 : ",hex(Z1))
        print(" X2 : ",hex(X2))
        print(" Z2 : ",hex(Z2))
        X1,Z1,X2,Z2 = x25519_ladder_step(X1,Z1,X2,Z2,x1,A24,p)
        print(" After Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        print(" X1 : ",hex(X1))
        print(" Z1 : ",hex(Z1))
        print(" X2 : ",hex(X2))
        print(" Z2 : ",hex(Z2))
        i = i - 1
    return(X1,Z1)

def ecc_mul_x25519_no_mask(x1,scalar, A24, p):
    # mask scalar
    # clear 255-th bit, and set 254-th bit
    #print(" b4 mask scalar : ",hex(scalar))
    print(" after mask scalar : ",hex(scalar))
    X1 = x1
    Z1 = 1
    X2 = 1
    Z2 = 0
    pp = 0
    i = 0
    while (scalar>0):
        print(" i = ",i)
        b = (scalar&1)
        c = b ^ pp
        pp = b
        X1,X2 = cswap(X1,X2,c)
        Z1,Z2 = cswap(Z1,Z2,c)
        print(" scalar",i,"&1, ---------b = ",b,"     c= ",c, "   pp=",pp);
        print(" Before Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        print(" xP : ",hex(x1))
        print(" X1 : ",hex(X1))
        print(" Z1 : ",hex(Z1))
        print(" X2 : ",hex(X2))
        print(" Z2 : ",hex(Z2))
        X1,Z1,X2,Z2 = x25519_ladder_step(X1,Z1,X2,Z2,x1,A24,p)
        print(" After Ladder Step i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        print(" X1 : ",hex(X1))
        print(" Z1 : ",hex(Z1))
        print(" X2 : ",hex(X2))
        print(" Z2 : ",hex(Z2))
        scalar = scalar // 2
        i = i + 1
    return(X1,Z1)



def ecc_mul_x448(x1,scalar, A24, p):
    # mask scalar
    # set 447-th bit, and clear 1,0th bits 
    #print(" b4 mask scalar : ",hex(scalar))
    mask1 = 0x8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    mask2 = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffc
    scalar = scalar | mask1
    scalar = scalar & mask2
    #print(" after mask scalar : ",hex(scalar))
    X1 = 1
    Z1 = 0
    X2 = x1
    Z2 = 1
    pp = 0
    i = 447
    while (i>=0):
        b = ((scalar>>i)&1)
        c = b ^ pp
        #print(" scalar>>",i,"&1, ---------b = ",b,"     c= ",c, "   pp=",pp);
        pp = b
        X1,X2 = cswap(X1,X2,c)
        Z1,Z2 = cswap(Z1,Z2,c)
        X1,Z1,X2,Z2 = x25519_ladder_step(X1,Z1,X2,Z2,x1,A24,p)
        #print(" after i = ",i," iteration, ladder_step has X1,Z1,X2,Z2 : ")
        #print(hex(X1))
        #print(hex(Z1))
        #print(hex(X2))
        #print(hex(Z2))
        i = i - 1
    return(X1,Z1)



# from RFC-8032, Sec. 5.1.1
def sqrt_25519(a):
    p = 2**255 - 19
    #print("\n ---------------------------------------")
    minus_a = -a % p
    x = pow(a, (p+3)//8, p)
    x2 = (x*x) % p
    print(" a : ",hex(a))
    print(" -a : ",hex(minus_a))
    print(" x = a ^ (p+3)//8 mod p  : ",hex(x))
    print(" x^2 : ",hex(x2))
    if  x2 == a:
        print(" x^2 == a : ")
        sqrt_x = x
    elif x2 == minus_a:
        print(" x^2 == -a : ")
        print(" sqrt_x = (pow(2,(p-1)//4,p)*x)%p ")
        sqrt_x = (pow(2,(p-1)//4,p)*x)%p
    return sqrt_x

