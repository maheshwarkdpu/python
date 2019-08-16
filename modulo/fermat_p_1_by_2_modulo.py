

p = 29

for a in range(1,p):
    print(a,"^",(p-1)>>1," mod",p," = ",(pow(a,(p-1)>>1,p)))

#https://crypto.stanford.edu/pbc/notes/numbertheory/


