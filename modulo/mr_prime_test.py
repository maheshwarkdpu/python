
#p = 0xf1d84d5e368114fff83c0c8a4b7ebefa574af2f662b642715719632868eca9b437dfd2c63c5f411eacb9b9dfca56c6ec14534a6c451c887e9bda00e20ef0ce640219f36fc7b7e5ddbeef867fc0df02c2b2feaab4bf79de43a241c12a87c62a32936acd88cd1ad790c3905fe62954448042a816b9f0d5dcfb196a93ae7e7e8f7d

p = 0xe021757c777288dacfe67cb2e59dc02c70a8cebf56262336592c18dcf466e0a4ed405318ac406bd79eca29183901a557db556dd06f7c6bea175dcb8460b6b1bc05832b01eedf86463238b7cb6643deef66bc4f57bf8ff7ec7c4b8a8af14f478980aabedd42afa530ca47849f0151b7736aa4cd2ff37f322a9034de791ebe3f51


a = 2**255

# Fermat littile theorem   a^p mod p = a
# Fermat littile theorem   a^(p-1) mod p = 1


b = pow(a,p,p)
print(hex(b))


b = pow(a,p-1,p)
print(hex(b))


p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
g = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
a = p-3

print(" a^g mod p = ", hex(pow(a,g,p)))
b = pow(a,(p-1)>>1,p)
print(hex(b))

