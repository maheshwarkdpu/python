#! /usr/bin/python3.6
import sys
from ecc_lib import *
from mont_ecc_lib import *
import random
import time

debug = 0
###################################################################

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, m):
	g, x, y = egcd(a, m)
	if g != 1:
		raise Exception('modular inverse does not exist')
	else:
		return x % m

def modular_sqrt(a, p):
	""" Find a quadratic residue (mod p) of 'a'. p
		must be an odd prime.

		Solve the congruence of the form:
			x^2 = a (mod p)
		And returns x. Note that p - x is also a root.

		0 is returned is no square root exists for
		these a and p.

		The Tonelli-Shanks algorithm is used (except
		for some simple cases in which the solution
		is known from an identity). This algorithm
		runs in polynomial time (unless the
		generalized Riemann hypothesis is false).
	"""
	# Simple cases
	#
	if legendre_symbol(a, p) != 1:
		return 0
	elif a == 0:
		return 0
	elif p == 2:
		return p
	elif p % 4 == 3:
		return pow(a, (p + 1) // 4, p)

	# Partition p-1 to s * 2^e for an odd s (i.e.
	# reduce all the powers of 2 from p-1)
	#
	s = p - 1
	e = 0
	while s % 2 == 0:
		s /= 2
		e += 1

	# Find some 'n' with a legendre symbol n|p = -1.
	# Shouldn't take long.
	#
	n = 2
	while legendre_symbol(n, p) != -1:
		n += 1

	# Here be dragons!
	# Read the paper "Square roots from 1; 24, 51,
	# 10 to Dan Shanks" by Ezra Brown for more
	# information
	#

	# x is a guess of the square root that gets better
	# with each iteration.
	# b is the "fudge factor" - by how much we're off
	# with the guess. The invariant x^2 = ab (mod p)gx_w = (9 + a_m/3)%p
	# is maintained throughout the loop.
	# g is used for successive powers of n to update
	# both a and b
	# r is the exponent - decreases with each update
	#
	x = pow(a, (s + 1) // 2, p)
	b = pow(a, s, p)
	g = pow(n, s, p)
	r = e

	while True:
		t = b
		m = 0
		for m in xrange(r):
			if t == 1:
				break
			t = pow(t, 2, p)

		if m == 0:
			return x

		gs = pow(g, 2 ** (r - m - 1), p)
		g = (gs * gs) % p
		x = (x * gs) % p
		b = (b * g) % p
		r = m


def legendre_symbol(a, p):
	""" Compute the Legendre symbol a|p using
		Euler's criterion. p is a prime, a is
		relatively prime to p (if p divides
		a, then a|p = 0)

		Returns 1 if a has a square root modulo
		p, -1 otherwise.
	"""
	ls = pow(a, (p - 1) // 2, p)
	return -1 if ls == p - 1 else ls

#####################################################################

def montgomery_gen_mul_448(u, scalar, prime, prime_len, a_wei, b_wei, a_mont, mask_and, mask_or):

    # Montgomery input(u, scalar)
    #Step 1: Convert montgomery u to weierstrass(x,y) coordinates

    #Step 1.1 : Convert u to big endian
    u_bytes = u.to_bytes(prime_len, byteorder='little')
    u_BE = int.from_bytes(u_bytes, byteorder='big')

    x = (u_BE + a_mont * modinv(3,prime))%prime
    y2 = pow(x,3) + a_wei*x + b_wei
    y2 = y2 % prime
    y = modular_sqrt(y2,prime)
    z = 0x01
    if(debug):
        print("Mont input u : ", hex(u))
        print("Wei_input_x : ", hex(x))
        print("Wei_input_y : ", hex(y))
        print("Wei_input_z : ", hex(z))

    #Step 2: Multiply in weierstrass coodinates (generic  mul)
    scalar_bytes = scalar.to_bytes(prime_len, byteorder='little')
    scalar_bignum = int.from_bytes(scalar_bytes, byteorder='big')
    if(debug):
        print("scalar little endian : ", hex(scalar))
        print("scalar big endian : ", hex(scalar_bignum))


    #Step 2.1 : Mask scalar as specified by RFC7748
    scalar_bignum = scalar_bignum | mask_or
    scalar_bignum = scalar_bignum & mask_and

    if(debug):
        print("scalar after mask : ", hex(scalar_bignum))

    #Step 2.2 : Call weierstrass mul call (generic)
    rx, ry, rz = ecc_mul(x, y, z, scalar_bignum, a_wei, prime)
    inv_rz = pow(rz,(prime-2),prime)
    rx = (rx * inv_rz)%prime
    ry = (ry * inv_rz)%prime
    Qx = rx
    Qy = ry
    Qz = (rz * inv_rz)%prime
    if(debug):
        print(" Qx = ", hex(Qx))
        print(" Qy = ", hex(Qy))
        print(" Qz = ", hex(Qz))


    #Step 3: Convert resultant Qx to montgomery coordinates
    x = (Qx - a_mont * modinv(3, prime))%prime
    if(debug):
        print("Resultant x in mont: ", hex(x))

    #Convert to little endian
    x_bytes = x.to_bytes(prime_len, byteorder='big')
    x = int.from_bytes(x_bytes, byteorder='little')
    if(debug):
        print("Mul Result x : ", hex(x))
    return x



def montgomery_mul_448(x1, scalar):
    p = 2**448 - 2**224 - 1
    A24 = 0x98AA

    byte_x1 = x1.to_bytes(56,byteorder='little') 
    x1 = int.from_bytes(byte_x1, byteorder='big')

    byte_scalar = scalar.to_bytes(56,byteorder='little') 
    int_scalar = int.from_bytes(byte_scalar, byteorder='big')
#    print("\n Prime                : ", hex(p))
#    print("\n Base Point           : ", hex(x1))
#    print("\n scalar               : ", hex(scalar))
#    print("\n scalar after big_num : ",hex(int_scalar))

    rx,rz = ecc_mul_x448(x1,int_scalar,A24,p)
    inv_rz = pow(rz,(p-2),p)
    rx = (rx * inv_rz)%p
    byte_rx  = rx.to_bytes(56,byteorder='big')
    int_rx  = int.from_bytes(byte_rx,byteorder='little')
    return int_rx


############################################################# 448 support ###################################################333
p_448 = pow(2,448) - pow(2,224) - 1    # 2^448 - 2^224 - 1
a_m_448 = 156326 
b_m_448 = 1

interim_a_numerator = 3-pow(a_m_448,2,p_448)
interim_a_denominator = 3*pow(b_m_448,2,p_448)
interim_a_denominator = modinv(interim_a_denominator,p_448)
a_w_448 = interim_a_numerator * interim_a_denominator # This IS multiplcation, since its modular inverse
a_w_448 = a_w_448 % p_448

interim_b_numerator = 2*pow(a_m_448,3,p_448)-9*a_m_448
interim_b_denominator = 27 * pow(b_m_448,3,p_448)
interim_b_denominator = modinv(interim_b_denominator, p_448)
b_w_448 = interim_b_numerator * interim_b_denominator # This IS multiplcation, since its modular inverse
b_w_448 = b_w_448 % p_448

mask_or_448 = 0x8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
mask_and_448 = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffC
prime_len_448 = 56

############################################################# 25519 support ###################################################

p_256 = pow(2,255)-19
a_m_256 = 486662 
b_m_256 = 1

interim_a_numerator = 3-pow(a_m_256, 2, p_256)
interim_a_denominator = 3*pow(b_m_256, 2, p_256)
interim_a_denominator = modinv(interim_a_denominator,p_256)
a_w_256 = interim_a_numerator * interim_a_denominator
a_w_256 = a_w_256 % p_256

interim_b_numerator = 2*pow(a_m_256, 3, p_256)- 9*a_m_256
interim_b_denominator = 27 * pow(b_m_256, 3, p_256)
interim_b_denominator = modinv(interim_b_denominator, p_256)
b_w_256 = interim_b_numerator * interim_b_denominator
b_w_256 = b_w_256 % p_256


mask_or_256 = 0x9000000000000000000000000000000000000000000000000000000000000000
mask_and_256 = 0x7ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff8
prime_len_256 = 32

if __name__ == "__main__":


    u = 0x500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
##    scalar = 0x9a8f4925d1519f5775cf46b04b5800d4ee9ee8bae8bc5565d498c28dd9c9baf574a9419744897391006382a6f127ab1d9ac2d8c0a598726b
#
##    u = 0x500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
##    scalar = 0x1c306a7ac2a0e2e0990b294470cba339e6453772b075811d8fad0d1d6927c120bb5ee8972b0d3e21374c9c921b09d1b0366f10b65173992d
#
##    u = 0x9b08f7cc31b7e3e67d22d5aea121074a273bd2b83de09c63faa73d2c22c5d9bbc836647241d953d40c5b12da88120d53177f80e532c41fa0
##    scalar = 0x1c306a7ac2a0e2e0990b294470cba339e6453772b075811d8fad0d1d6927c120bb5ee8972b0d3e21374c9c921b09d1b0366f10b65173992d
#
#    u = 0x3eb7a829b0cd20f5bcfc0b599b6feccf6da4627107bdb0d4f345b43027d8b972fc3e34fb4232a13ca706dcb57aec3dae07bdc1c67bf33609
#    scalar = 0x9a8f4925d1519f5775cf46b04b5800d4ee9ee8bae8bc5565d498c28dd9c9baf574a9419744897391006382a6f127ab1d9ac2d8c0a598726b

#    u = random.randint(2, p_448)
#    scalar = random.randint(2, p_448)
    u = 0x0500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    scalar = 0x0500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    count=0
    flag = True
    while flag:


#        scalar = random.randint(2, p_448)
#        u = random.randint(2, p_448)
        count = count + 1
        print("\n--> Count : ", count)
#        print("\nu : ", hex(u))
#        print("scalar : ", hex(scalar))
        x = montgomery_gen_mul_448(u, scalar, p_448, prime_len_448, a_w_448, b_w_448, a_m_448, mask_and_448, mask_or_448)
        print("\n\t       Mul result : ", hex(x))

        x1 = montgomery_mul_448(u, scalar)
        print("\tMul ladder result : ", hex(x1))

        u = scalar
        scalar = x

#        input("\n") 
        if(count == 1000000):
            sys.exit(0)
#        time.sleep(1)
        if(x == x1):
            flag = True
#            u = x
        else:
            flag = False



    print(" Completed")
