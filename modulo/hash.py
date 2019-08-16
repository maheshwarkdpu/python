#! /usr/bin/python

import hashlib

import sys

lineno = 0
b=0
e=0
m=0
result=0

print("\n\n Usage: python3.7  hash.py < hash.txt \n\n")
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

    h = hashlib.sha256(line.encode('utf-8'))
    print("a = ",line," Hash(a) = ",h.hexdigest())
    #print(" -------------------------------------------------------------------------------------------")
print()




