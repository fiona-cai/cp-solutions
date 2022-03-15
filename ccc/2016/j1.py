#https://dmoj.ca/problem/ccc16j1
#CCC '16 J1 - Tournament Selection

a = input()
b = input()
c = input()
d = input()
e = input()
f = input()

w = 0
l = 0

if a == "W":
    w += 1
if b == "W":
    w += 1
if c == "W":
    w += 1
if d == "W":
    w += 1
if e == "W":
    w += 1
if f == "W":
    w += 1

if w == 0:
    print("-1")
elif w <= 2:
    print("3")
elif w <= 4:
    print("2")
else:
    print("1")
