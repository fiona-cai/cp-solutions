#https://dmoj.ca/problem/usaco19febb3
#USACO 2019 February Bronze P3 - Measuring Traffic

n = int(input())

minadd = 0
maxadd = 0
minsub = 0
maxsub = 0
start = [0, 1001]
roads = []
for _ in range(n):
    a,b,c = input().split()
    b = int(b)
    c  = int(c)
    roads.append([a,b,c])
    if a == "on":
        minadd += b
        maxadd += c
    elif a == "none":
        start[0] = max(start[0], b-maxadd+minsub)
        start[1] = min(start[1], c-minadd+maxsub)
    else:
        minsub += b
        maxsub += c

start[0] = max(0, start[0])
print(start[0], start[1])


for a,b,c in roads:
    if a == "on":
        start[0] += b
        start[1] += c
    elif a == "off":
        start[0] -= c
        start[1] -= b
        start[0], start[1] = max(0, start[0]), max(0, start[1])
    else:
        start[0], start[1] = max(b, start[0]),min(c, start[1])
print(start[0], start[1])
