

from ecc_lib import *



#v = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffff
p = 2**448 - 2**224 - 1

#x1 = 0x0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005
x1 = 0x936f37bc6c1bd07ae3dec7ab5dc06a73ca13242fb343efc72b9d82730b445f3d4b0bd077162a46dcfec6f9b590bfcbcf520cdb029a8b73e
scalar = 0x9a8f4925d1519f5775cf46b04b5800d4ee9ee8bae8bc5565d498c28dd9c9baf574a9419744897391006382a6f127ab1d9ac2d8c0a598726b
#scalar = 0x1c306a7ac2a0e2e0990b294470cba339e6453772b075811d8fad0d1d6927c120bb5ee8972b0d3e21374c9c921b09d1b0366f10b65173992d

A24 = 0x98AA


byte_scalar = scalar.to_bytes(56,byteorder='little')

int_scalar = int.from_bytes(byte_scalar, byteorder='big')
print("\n Prime                : ", hex(p))
print("\n Base Point           : ", hex(x1))
print("\n scalar               : ", hex(scalar))
print("\n scalar after big_num : ",hex(int_scalar))


rx,rz = ecc_mul_x448(x1,int_scalar,A24,p)

inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p


byte_rx  = rx.to_bytes(56,byteorder='big')
int_rx  = int.from_bytes(byte_rx,byteorder='little')

print("\n x448 result :")
print(" rx = ", hex(rx))
print(" int_x = ", hex(int_rx))
print(" z = ", hex((rz*inv_rz) % p))
print()


