
# Carmichael Numbers 561, 1105, 1729, 2465, 2821, 6601, 8911

p = 29 
count = 0

for a in range(1,p):
    x = pow(a,(p-1),p)
    print("a =", hex(a),",   ", a,"^",(p-1)," mod",p," = ",x)
    if(x == 1):
        count = count+1
print(" count = ", count)

#https://crypto.stanford.edu/pbc/notes/numbertheory/


