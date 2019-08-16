#! /usr/bin/python



import sys

lineno = 0
b=0
e=0
m=0
result=0

print("\n\n Usage: python3.7  mod_exp.py < mod_exp.txt \n\n")
while True:
    line = sys.stdin.readline()
    if not line:
        break
    lineno = lineno + 1
    if(line[0] == " "):
        continue

    if(line[0] == "\n"):
        continue

    if(line[0] == "#"):
        continue

    print(lineno)
    fields = line.split(":")
    #print("typeof(fields) = ", type(fields))
    #print(" fields : ", fields)
    #print("typeof(fields[0]) = ", type(fields[0]))
    #print("typeof(fields[1]) = ", type(fields[1]))
    #print("typeof(fields[2]) = ", type(fields[2]))
    #print(line[0:4])

    b = int(fields[0],16)
    e = int(fields[1],16)
    m = int(fields[2],16)
    #print("typeof(b) = ", type(b))
    #print("typeof(e) = ", type(e))
    #print("typeof(m) = ", type(m))
    print(" b = ", hex(b))
    print(" e = ", hex(e))
    e = e >> 1
    print(" e >> 1 = ", hex(e))
    print(" m = ", hex(m))
    result = pow(b,e,m)
    print(" Result = ",hex(result))
    print(" -------------------------------------------------------------------------------------------")
print()




