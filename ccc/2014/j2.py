#https://dmoj.ca/problem/ccc14j2
#CCC '14 J2 - Vote Count

n = int(input())
ab = input()
a = 0
b = 0

ablist = list(ab)

for x in ablist:
    if x == "A":
        a += 1
    if x == "B":
        b += 1

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")
