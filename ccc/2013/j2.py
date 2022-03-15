#https://dmoj.ca/problem/ccc13j2
#CCC '13 J2 - Rotating letters

ab = input()
a = 0
b = 0

ablist = list(ab)

for x in ablist:
    if x == "I":
        a += 1
    elif x == "O":
        a += 1
    elif x == "S":
        a += 1
    elif x == "H":
        a += 1
    elif x == "Z":
        a += 1
    elif x == "X":
        a += 1
    elif x == "N":
        a += 1
    else:
        b += 1

if b == 0:
    print("YES")
else:
    print("NO")
