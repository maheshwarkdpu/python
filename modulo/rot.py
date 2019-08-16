

#ROTL64(x,n)  =  SHL64(x,n) | SHR(x,(64-n))
#ROTL32(x,n)  =  SHL32(x,n) | SHR(x,(32-n))
#ROTL16(x,n)  =  SHL16(x,n) | SHR(x,(16-n))
#ROTL8(x,n)   =  SHL8(x,n)  | SHR(x,(8-n))


def rotl_64(x,n):
    return( ((x<<n)&0xffffffffffffffff) | (x >> (64-n)))


def rotl_8(x,n):
    return( ((x<<n)&0xff) | (x >> (8-n)))

a64 = 0x0102030405060708

a8  = 0x02

print("a64 = ",hex(a64))
print(" rot(a64,8) = ", hex(rotl_64(a64,8)))

print(" SHL(a64,8) = ",hex((a64<<8)&0xffffffffffffffff))
print(" SHR(a64,64-8) = ",hex((a64>>(64-8))))


