#https://dmoj.ca/problem/ccc14s2
#CCC '14 S2 - Assigning Partners

n = int(input())

partners = {}

partners1 = input().split()
partners2 = input().split()

work = True
for i in range(n):
    p1 = partners1[i]
    p2 = partners2[i]
    if p1 == p2:
        work = False
        break
    if p1 in partners:
        prevp2 = partners[p1]
        if prevp2 != p2:
            work = False
            break
    else:
        partners[p1] = p2
        partners[p2] = p1

if work:
    print("good")
else:
    print("bad")
