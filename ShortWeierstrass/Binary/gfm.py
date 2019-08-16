
import sys

from binary_ecc_lib import *

X=0x87b514cc01246af8ac95686a46edb60b
Y=0xe510282e01d129f7ef1ec86fdd83e5a1
#Y=0xdf199e8f8cb1a8b146bf63f2b718deea
#Y=0x470628a524e88a8aaba46ef51c126ccc

Z = gfm(X,Y)
print(" X=",hex(X),"   .   Y=",hex(Y), " =   Z=",hex(Z))
