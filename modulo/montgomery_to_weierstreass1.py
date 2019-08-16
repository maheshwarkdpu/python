# Python code
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
		return pow(a, (p + 1) >> 2, p)

	# Partition p-1 to s * 2^e for an odd s (i.e.
	# reduce all the powers of 2 from p-1)
	#
	s = p - 1
	e = 0
	while s % 2 == 0:
		s //= 2
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
	x = pow(a, (s + 1) >> 1, p)
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
	ls = pow(a, (p - 1) >> 1, p)
	return -1 if ls == p - 1 else ls

# Montgomery form Curve25519 parameters (b*y^2 = x^3 + a*x^2 + x (mod p))
# Change these for a a different Montgomery curve
p = pow(2,255)-19
a_m = 486662 
b_m = 1

# Here be dragons! This works, so don't really change it
interim_a_numerator = 3-pow(a_m,2)
interim_a_denominator = 3*pow(b_m,2)
interim_a_denominator = modinv(interim_a_denominator,p)
a_w = interim_a_numerator * interim_a_denominator # This IS multiplcation, since its modular inverse
a_w = a_w % p

interim_b_numerator = 2*pow(a_m,3)-9*a_m
interim_b_denominator = 27 * pow(b_m,3)
interim_b_denominator = modinv(interim_b_denominator, p)
b_w = interim_b_numerator * interim_b_denominator # This IS multiplcation, since its modular inverse
b_w = b_w % p

def mont_to_wei(x, p):
    x = (x + a_m * modinv(3,p))%p 
    return x

def wei_to_mont(x, p):
    x = (x - a_m * modinv(3, p))%p
    return x

def gen_y_in_wei(x, p):
    y2 = pow(x,3) + a_w*x + b_w
    y2 = y2 % p
    y = modular_sqrt(y2,p)
    return y



if __name__ == "__main__":
#    x = 9                                   # This is Curve25519 specific
#    x = 0x4c1cabd0a603a9103b35b326ec2466727c5fb124a4c19435db3030586768dbe6
    x =  0x4f2b886f147efcad4d67785bc843833f3735e4ecc2615bd3b4c17d7b7ddb9ede
    x = (x + a_m * modinv(3,p))%p           # This is needed, since we are doing a change of variables, so this is the analogous change.
    
    y2 = pow(x,3) + a_w*x + b_w
    y2 = y2 % p
    
    y = modular_sqrt(y2,p)
    
    print("P: " + hex(p))
    print("A: " + hex(a_w))
    print("B: " + hex(b_w))
    print("Gx: " + hex(x))
    print("Gy: " + hex(y))

    print("\n\n")

    print("P: " + hex(p))
    print("A: " + hex(a_w))
    print("B: " + hex(b_w))
    print("Gx: " + hex(mont_to_wei(9, p)))
    print("Gy: " + hex(gen_y_in_wei(mont_to_wei(9,p), p)))

    print("Doing weierstrass to montgomery")
    x = (x - a_m * modinv(3, p))%p
    print("u : " + hex(x))

#    Qx = 0x7d304d21ffb25effa21bc6f3ae7a96dcf9b3389cf8953f393b719447e202ff14
    Qx = 0x6cc1c0c8e7469b20de497bf273cc298acfb9e02b9ee6391d8bd8794f064a819b 
#    Qx =  0x6a2ee33d62a0de5d95aff5ef0a17b39d1c64ffd3383efc8af6f5842e9d177d4f
    print("\n\nQx: " + hex(Qx))
    print("Qx in mont: " + hex(wei_to_mont(Qx, p)))

