

from ecc_lib import *




p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = p - 3
p256_fpm_table = [
    [0x0000000000000000000000000000000000000000000000000000000000000001,
     0x0000000000000000000000000000000000000000000000000000000000000001,
     0x0000000000000000000000000000000000000000000000000000000000000000],

    [0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
     0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5,
     0x0000000000000000000000000000000000000000000000000000000000000001],

    [0x74aea555a68379c912b559ea124a2afcc5bd66a57bf3d63efe730749ae6dc1ad,
     0x7e88e5e6a142d5c2269f21a158e82ab2c79fcecb26e397b96fd5b9fbcd0a69a5,
     0x744a5475b524565578af2dc675105a4918e25a670804d71efb9688a7ae2215d2],

    [0x91f273bf65653069451d10fde598ca851714bd30cfea7d01e0ab3a3da85f296e,
     0x5bc3c3afada8f5f062cd7e9a68e3744f063b82b1c226a207bf248c5a1ba2e40a,
     0x2fa118d60c6baa0c945ea55e5f642ea12e0d148ef60121013d16569489281a72],

    [0x8c1def2011089791d8685b5acf05c0770aa2ee79db1ba9cbe71d7e1d910f2e5c,
     0x14f1edaeb8e9c8d4797d164a3946c7ff50a7c8cd59139a4dbce354e6e4df09c3,
     0x7b283f27e933d5cb592f916f280c5b2b5c9ebac230aa4a7e519a483e65f859e5],

    [0x78e45e821995c9578c314b2b5f571eac185da0ca5478580141ed966062b2456d,
     0xff3e98ff9ee1bb9aee6b3d83fa0d7318875649c110bb46aee47d494b54f809bf,
     0xc45c8fab73d76d622ec3faac66539260cfa82e779450f228ac715167ea7bdff9],

    [0x62857f8d06c3475d10259c240fa782036130d31016236f14bc2956a01b53fa7c,
     0x93ee2f5a765cfd4b3754bb1f636d3bff2d5e8419edac368519fc06548d8e988d,
     0x2141c44053b10d5d2864ee9364703b56de452c0b4bba1e90c1dbc529c1ab054d],

    [0x300a46d97d386d44d1a643988fa692ee636eddd8866f2cace91349d26f18aeec,
     0xc9adfe4cf22fff6a1831c6b6055a6ee51e9a5a57c8054d9e054620f86626f24c,
     0x068fdd9400b9c0134aee1e27b7bead8b9881954048d3eddba4f5a09b5237148b],

    [0xec5497f5a0908694bacc7d8a4dc23143a4e9cbed27de6386bd34c5c461f52e9f,
     0x1eddaf51836859e1369f1ae8d9ab02e4123b6f151d9b796e297a38fa5613d9bc,
     0x2a15d08e20dc76662792052277478aa58f4476213b3789138d9e49eee72d6ff2],

    [0xac45e893290b17e1521cccde83e802d513be09b2e8a0a314cac26f3eea764302,
     0xa291cbe81ac4ce611770a081da4a2c657a4b6d2c7a6a1ae571166155da0d6d3f,
     0x09e32bfa8a160cae8a8d24733fadd9a320f23353cb1f228fe774c3c222b7c409],

    [0xdae6d2b0d7ee6ad71f01495e87e4c3a0e2d09e0a81967cf485bebf26c540ee39,
     0x0261de5197f0e709659e6ab3d8c2a2dc92f4ca12fc695c193f2a1612c843aa5f,
     0x53cc83b7e582fb03f963ce310c852a14a5d026da30e249e9b208d8900942f871],

    [0x34b60e13b5496be3ced93c1bc8a9e5220eba4d40c462e812f6f0bd65bc167b4f,
     0xc60e84aafe2eebaf1312b66d533bc9208228ada4aa1685cf015c0ec4a6f08128,
     0x5842cdad9a15a193b233b30eb4c948bd0870e16d54d97e5b16da2c25545df835],

    [0xf20524a37e463deaa353356acbafbf493dba167935ad36d3262305adadeaa316,
     0xe0b328d5a501f4cb1cc013df42865ee46c4aca1dfc1856fd48583cd29455fa37,
     0xf37b1d1d51d7f1e98b9132ba5e659371062e4e63f27516acf2f94cbc50035cb8],

    [0xacc6e4048e6fc2adae97bbb2aed840311365972366132c46a8dcd2d362449a9a,
     0x57f16f5e4dfc451ad0ecd767d73ddcf0b4e1e1c0290f07a5949d80b3681c4ba1,
     0x441c0b9b2dfe4cafde342febf7a22be2d5cdb3ee8a7f88a59f199b2d6ae45642],

    [0xd59bb2bfc3017806af955db3fcca26a58e3c5c806c98ec6420f56775f41197e1,
     0x7c653c2f8b21698960dcc77dd7236964d27bb976d9fc43ce7d50a3b406f9c6aa,
     0x29600b61d087ba2a5929de16b9ca49d9e336d923fab8dd9125d435860a4ff4f2],

    [0xc4f893c3152667230d19919e01ce782852bd24f58174e016f88a0056fd94d279,
     0xeb50cf11694bd2f44c3856a19a8e25dd05ab8c2ba241a632a8cc655c17eb808c,
     0x30f7b0235ea4ccb07823833a24c1888310ade2cb685caf466708015999b64154]
        ]


#scalar = 0xc51e4753afdec1e6b6c6a5b992f43f8dd0c7a8933072708b6522468b2ffb06fd
scalar = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632552
#scalar = 0x0000000000000000000000000000000000000000000000000000000000000003



# From GuidetoEllipticCurveCryptography.pdf
# Algorthm 3.44 Fixed-base comb method for point multiplication
#INPUT: Window width w, d = t/w, k = (kt−1, . . ., k1, k0)2, P ∈ E(Fq ).
#OUTPUT: kP.
#1. Precomputation. Compute [aw−1, . . .,a1,a0]P for all bit strings (aw−1, . . ., a1,a0) of length w.
#2. By padding k on the left with 0s if necessary, write k = Kw−1 · · ·K1K0, where each K j is a bit string of length d. Let K j i denote the i th bit of K j .
#3. Q←∞.
#4. For i from d −1 downto 0 do
#   4.1 Q←2Q.
#   4.2 Q←Q +[Kw−1 i , . . ., K1 i , K0 i ]P.
#5. Return(Q).




d = 256>>2  #d = 256/4
i=d-1
rx = 1
ry = 1
rz = 0
while(i>=0):
    c0 = (scalar>>i)&1
    c1 = (scalar>>(i+d))&1
    c2 = (scalar>>(i+(d<<1)))&1
    c3 = (scalar>>(i+(d<<2)-(d)))&1
    combination = (c3<<3) | (c2<<2) | (c1<<1) | (c0<<0)
    print(" c3",c3," c2=",c2," c1=",c1," c0= ",c0)
    print(" iteration = ",i," combination = ", hex(combination))

    print("double inputs : ")
    print("rx : ",hex(rx))
    print("ry : ",hex(ry))
    print("rz : ",hex(rz))
    rx,ry,rz = ecc_double_jacobian(rx,ry,rz,a,p)

    px = p256_fpm_table[combination][0]
    py = p256_fpm_table[combination][1]
    pz = p256_fpm_table[combination][2]

    print("add inputs : ")
    print("rx : ",hex(rx))
    print("ry : ",hex(ry))
    print("rz : ",hex(rz))
    print("px : ",hex(px))
    print("py : ",hex(py))
    print("pz : ",hex(pz))
    rx,ry,rz = ecc_add_jacobian(rx,ry,rz,px,py,pz,a,p)

    i-=1

print("after ecc_mul : X,Y,Z")
print(" x = ", hex(rx))
print(" y = ", hex(ry))
print(" z = ", hex(rz))

inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz*inv_rz)%p
ry = (ry * inv_rz*inv_rz*inv_rz)%p
print("\n mul result :")
print(" x = ", hex(rx))
print(" y = ", hex(ry))
print(" z = ", hex((rz*inv_rz) % p))
print()



