

from ecc_lib import *




p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = p - 3
x1 = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
y1 = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
z1 = 0x0000000000000000000000000000000000000000000000000000000000000001

array = [[1,1,0],[1,1,0],[1,1,0],[1,1,0]]
px = x1
py = y1
pz = z1

#   //window size is 4
#   //prime length in bytes
#   if      (prime_length == 24) { d = 192/4; }  /* Curve P192 */
#   if      (prime_length == 28) { d = 256/4; }  /* Curve P224 */
#   else if (prime_length == 32) { d = 256/4; }  /* Curve P256 */
#   else if (prime_length == 48) { d = 384/4; }  /* Curve P384 */
#   else if (prime_length == 66) { d = 576/4; }  /* Curve P384 */
#
#   if (prime_length < 48) len = 6*8; //48;
#   else if (prime_length == 48) len = 7*8; //56;
#   else if (prime_length > 48)  len = 9*8; //72;
#   primelength = prime_length;
d = 256>>2


#//      Compute the 4 co-efficiants 	P, 
#//      				(2^d)*P, 
#//      				(2^(2*d))*P 
#//      				(2^(3*d))*P
#//                  where d = (t/w) t=256/384 w=4. Place at PRE_COFFS
#//
#//
#// 2^(d-1)*P , . . . . . . . . . . . .  . . . . . . . . . . . , P
#// 2^(2d-1)*P, . . . . . . . . . . . .  . . . . . . . . . . . , 2^(1*d)*P
#// 2^(3d-1)*P, . . . . . . . . . . . .  . . . . . . . . . . . , 2^(2*d)*P
#// 2^(4d-1)*P, . . . . . . . . . . . .  . . . . . . . . . . . , 2^(3*d)*P
#//
#//			i.e
#//
#//Example m=256, w =4, and d = (m/w) = (256/4) = 64
#//
#// 2^(63)*P , . . . . . . . . . . . .  . . . . . . . . . . . , P
#// 2^(127)*P, . . . . . . . . . . . .  . . . . . . . . . . . , 2^(64)*P
#// 2^(191)*P, . . . . . . . . . . . .  . . . . . . . . . . . , 2^(2*64)*P
#// 2^(255)*P, . . . . . . . . . . . .  . . . . . . . . . . . , 2^(3*64)*P
#//								|
#//								|
#//							     co-efficiants
j=0
while(j<4): #	/* 4 co-efficiants  */
    #/* Set each co-efficiant into an array */
    array[j][0] = px
    array[j][1] = py
    array[j][2] = pz
    if(j == 3):
        break
    #// below loop computes (2^64)*P, (2^(2*64))*P, (2^(3*64))*P,
    #//
    #// Example to calculate (2^64)*P
    #//		=  P
    #//		=    P +   P  =    2P  =  (2^1)*P
    #//		=   2P +  2P  =    4P  =  (2^2)*P
    #//		=   4P +  4P  =    8P  =  (2^3)*P
    #//		=   8P +  8P  =   16P  =  (2^4)*P
    #//		=  16P + 16P  =   32P  =  (2^5)*P
    #//		.
    #//		.
    #//		.
    #//		64 times ...
    #//		=  (2^64)*P
    #//
    #// Example to calculate (2^(2*64))*P
    #// Assume what you got final result above as P and do step as above.
    i=0
    while(i<d): #	//d = (t/w) = (256/384)/4 = 64/96 times
        #EC_POINT_dbl(group, R, P, ctx);
        #EC_POINT_copy(P,R);
        rx,ry,rz = ecc_double_jacobian(px,py,pz,a,p)
        px = rx
        py = ry
        pz = rz
        i+=1
    j+=1
print(" Array START \n")
j=0
while(j<4): 
    print(hex(array[j][0]))
    print(hex(array[j][1]))
    print(hex(array[j][2]))
    print("\n")
    j+=1
print(" Array ENDS \n")
#//					if d = 64
#//Now x[0] and y[0] has (2^(0*d))*P	=  P
#//	 x[1] and y[1] has (2^(1*d))*P	= (2^64)*P
#//	 x[2] and y[2] has (2^(2*d))*P	= (2^(2*64))*P
#//	 x[3] and y[3] has (2^(3*d))*P	= (2^(3*64))*P
#//
#//Let x[0] and y[0] as P0
#//	 x[1] and y[1] as P1
#//	 x[2] and y[2] as P2
#//	 x[3] and y[3] as P3
#//
#//compute the points
#//	Q(15) + (Q(15)+Q(14)) + (Q(15)+Q(14)+Q(13)) + ...  14 terms
#//
#//
#//The following loop computes 
#//For each loop set R <-- 0
#//For i =  1 ==>  0x0001   computes 	R <-- R + P0
#//For i =  2 ==>  0x0010   computes 	R <-- R + P1
#//For i =  3 ==>  0x0011   computes 	R <-- R + P0 + P1
#//For i =  4 ==>  0x0100   computes 	R <-- R + P2
#//For i =  5 ==>  0x0101   computes 	R <-- R + P0 + P2
#//For i =  6 ==>  0x0110   computes 	R <-- R + P1 + P2
#//For i =  7 ==>  0x0111   computes 	R <-- R + P0 + P1 + P2
#//For i =  8 ==>  0x1000   computes 	R <-- R + P3
#//For i =  9 ==>  0x1001   computes 	R <-- R + P0 + P3
#//For i = 10 ==>  0x1010   computes 	R <-- R + P1 + P3
#//For i = 11 ==>  0x1011   computes 	R <-- R + P0 + P1 + P3
#//For i = 12 ==>  0x1100   computes 	R <-- R + P2 + P3
#//For i = 13 ==>  0x1101   computes 	R <-- R + P0 + P2 + P3
#//For i = 14 ==>  0x1110   computes 	R <-- R + P1 + P2 + P3
#//For i = 15 ==>  0x1111   computes 	R <-- R + P0 + P1 + P2 + P3
#//
#//
#//Since window = 4 and with [a3,a2,a1,a0] there are 1 to ((2^w) - 1)
#//i.e 1 to 15 points are needed for calculating kP
i=1
while(i<16): 
    #EC_POINT_set_to_infinity(group, R);	//R <-- O;	//set to infinity
    rx = 1
    ry = 1
    rz = 0
    j=0
    while(j<4):
        #//it check no. of bits in "i" variabe.
        #//if i(j) == 1  then R = R + P
        if((i>>j) & 1):
            #print("i = ", i, "j = ", j)
            #print(i>>j)
            #EC_POINT_set_affine_coordinates_GFp(group,P,x[j],y[j],ctx);		//set P <--- (x[j],y[j])
            px = array[j][0]
            py = array[j][1]
            pz = array[j][2]
            #EC_POINT_add(group, R, R, P, ctx);	//R <-- R + P
            rx,ry,rz = ecc_add_jacobian(rx,ry,rz,px,py,pz,a,p)

            #inv_rz = pow(rz,(p-2),p)
            #rx = (rx * inv_rz*inv_rz)%p
            #ry = (ry * inv_rz*inv_rz*inv_rz)%p
            #rz = (rz * inv_rz)%p
        j+=1
    print("i = ", i)
    print("x = ",hex(rx))
    print("y = ",hex(ry))
    print("z = ",hex(rz))
    print("\n")
    i+=1



