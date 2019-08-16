

from ecc_lib import *




p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = p - 3
p256_fpm_table = [
    [0x0000000000000000000000000000000000000000000000000000000000000000,
     0x0000000000000000000000000000000000000000000000000000000000000001,
     0x0000000000000000000000000000000000000000000000000000000000000000],

    [0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296,
     0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5,
     0x0000000000000000000000000000000000000000000000000000000000000001],

    [0x8f22820598a60fe3c582a4e4e495f2997b48a1de965059a918c3c50bb251a29d,
     0x468ab3e51fcb47229871e7e95bf28286cd448ed3eb0c78ecd34eac121d285bc2,
     0xc297492c20cce4966ae2cd2b58b75e48ffbd548995ef960d41e274dc1e5b3ed6],

    [0x0bad26fbd93b1ab7e8448e98e098c19f90e3156a94ae76e356e8bcaa5d210197,
     0x4a1d6bbedf46a06f7d7618287a69fd83346c8ed1ef774189b0e3613855bd8d83,
     0x30939029db21454321313957aec9c854a4b23170b0cee4c46f2ec46cdf0d9342],

    [0xe1aa8f7141bfe1ed0ab485599b5779ebec8b93533c5bde62423df00d2b1cb5f2,
     0xd2f122ef803850478290ab2a627771ec4eccef6334a3d343c0a9f7e656103895,
     0x9182b5003bc1da72e3be14e0fb0c2593330522bd83326ee2e2457d8e6de1783e],

    [0x6a140c5570ae60a61eab131df0a7b9955ca52eee3a03b007a6fc97e60ddcd000,
     0x32665be0dea111a9f1de8948b01514c36e693babf68c4db9ed6307a3e9ec3df5,
     0xc53bb6c40c028674ca4dbb66216624f8939409db2e75d7fa62d4b5e6a8870ac3],

    [0xcca15363506327c1cb6a22b45277e102279482b5edc0aff9a43c31e5ee4c7f21,
     0x5f70630191f1e4f4a011b40220423775f79c950c421df6a003e867c64d00c6a6,
     0xd1c592c6f4fc29af17c2bd51f6c8a5ea99169413cc8fbce78d146d2131592204],

    [0xf8af31df7a189eddb7a3dec5822322ab68811a4ab165dd6216e93beda6327b8f,
     0x4f09a05fac180f4162aa8320e134a671366e374fff2a669868ee233e77bf98d2,
     0xc13ed81bdf7bdf9f50f3b9938aed53978b06ec6c01b7c15111c42b813f40f476],

    [0x3d01d0abc5953e53e5d138e3d692d41a616f5757559bc2d92888c2bcc4e2afba,
     0x193f2d8a1f2eb2048247f138028cf01a45ce26236dd5a56f707435768cdfbfbf,
     0x4a03bfe85bdb2daa2679f90708a92d0dd6ca89397a68fb2df14a32d808ed7f2f],

    [0x339d35143ab7894b6d62618d19a5f8d6bc4cb6e52a11ea88c6bba46d0ca352d1,
     0xdc93a482de79b6945961a59fde2670e04efacd9fa462ea514b7dc4a3c108c7bb,
     0xce26909e040d04a81f890e57c1da36056fcc9c5b6e870e7ddbefc849c4167fe7],

    [0xfd00adb9b97301c9a9cc2bcc6007da4f30ec4dbf31259407ba732617928f48bb,
     0x880df7592b7b4d98b051aed93df1dddc56c93d8f17148250867c1c89c3bfd08b,
     0xfcae15e2dc42b476c8c68143cfcc9446a73fea0145370be09e1d98cbe781fd4b],

    [0xd2015a57f4f6398fb1e1d1914a7841e7463c9536c59ce39d41f55168e5be91e1,
     0x06b9ac4a0b8a2038ae8645b74673263083f58c9fdc2715a411cd96d46ae3edb0,
     0x2a8b67f7e0526c090cea0b002ebf997d85d2d9d676007cca264536cc109cee08],

    [0xffcb0a9a7dfe6606eecf47ad4c3c4a4e39a621a3c310b661115a03356f55f312,
     0xe572e4df83286cb40ddea98c8958c6b3aa0751fab23793d87f73946ec5ccf9f8,
     0xef20af4e7295b11e8f6d3d02240a3dac0349cce0f30b0638136b84c0966e7415],

    [0xc94d5b90b318d9ea9dd271891ae71799bf5ce7a4d629696ea97d5e617021cf29,
     0x56f3c6fecafa2a290159021d82bd1799ff6974d15e49646b5dea5f0b32e88933,
     0x1c1353015f858c204d4352f5c186b6ca582f44e2c250446a49733d20aadce543],

    [0xbe6e27b32cdf8dbafc1056e59f0a28b21b69f4ba15cd8668702aa678a2977270,
     0x7f5b34267b6a8b10fbf97ffdc6fde4b34e959e1da067b6e1869c4fbe272ab43a,
     0xe3892e89b6d2b79db0e0674d1287752e66d42cc6abe0db835de74ac49c6d041d],

    [0x24366156cb659023f21be5dda2b9fe84b402833f46a7b876b9488cde4727a595,
     0xf0fa6956d8c7af3ee73bc2d4ec911c8f37442d407daad19ca47910e1a5c5e688,
     0x5884f036bd33a6576f1f822e6fb9caa5fdd2a20ec14bde4de2d3ef31af4554fb],
        ]


#scalar = 0xc51e4753afdec1e6b6c6a5b992f43f8dd0c7a8933072708b6522468b2ffb06fd
scalar = 0xFFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632552
#scalar = 0x0000000000000000000000000000000000000000000000000000000000000002



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
rx = 0
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
    rx,ry,rz = ecc_double(rx,ry,rz,a,p)

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
    rx,ry,rz = ecc_add(rx,ry,rz,px,py,pz,a,p)

    i-=1

print("after ecc_mul : X,Y,Z")
print(" x = ", hex(rx))
print(" y = ", hex(ry))
print(" z = ", hex(rz))

inv_rz = pow(rz,(p-2),p)
rx = (rx * inv_rz)%p
ry = (ry * inv_rz)%p
print("\n mul result :")
print(" x = ", hex(rx))
print(" y = ", hex(ry))
print(" z = ", hex((rz*inv_rz) % p))
print()



