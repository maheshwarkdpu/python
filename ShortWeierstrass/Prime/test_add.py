

from ecc_lib import *




p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = p - 3
x1 = 0xde2444bebc8d36e682edd27e0f271508617519b3221a8fa0b77cab3989da97c9
y1 = 0xc093ae7ff36e5380fc01a5aad1e66659702de80f53cec576b6350b243042a256
z1 = 0x0000000000000000000000000000000000000000000000000000000000000001


x2 = 0x0000000000000000000000000000000000000000000000000000000000000001
y2 = 0x0000000000000000000000000000000000000000000000000000000000000001
z2 = 0x0000000000000000000000000000000000000000000000000000000000000000

#x2 =  0x7669e6901606ee3ba1a8eef1e0024c33df6c22f3b17481b82a860ffcdb6127b0
#y2 =  0xfa878162187a54f6c39f6ee0072f33de389ef3eecd03023de10ca2c1db61d0c7
#z2 = 0x0000000000000000000000000000000000000000000000000000000000000001

print("\n add input X,Y,Z :")
print(" X = ", hex(x1))
print(" Y = ", hex(y1))
print(" Z = ", hex(z1))
print(" X = ", hex(x2))
print(" Y = ", hex(y2))
print(" Z = ", hex(z2))
rx,ry,rz = ecc_add_jacobian(x1,y1,z1,x2,y2,z2,a,p)
print("\n add result X,Y,Z :")
print(" X = ", hex(rx))
print(" Y = ", hex(ry))
print(" Z = ", hex(rz))


inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
ry = (ry * inv_rz)%p
print("\n add result :")
print(" x = ", hex(rx))
print(" y = ", hex(ry))
print(" z = ", hex((rz*inv_rz) % p))
print()


print()



