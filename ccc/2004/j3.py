#https://dmoj.ca/problem/ccc04j3
#CCC '04 J3 - Smile with Similes

adj = int(input())
n = int(input())

adjs = []
ns = []

while adj > 0:
    y = input()
    adjs.append(y)
    adj -= 1

while n > 0:
    y = input()
    ns.append(y)
    n -= 1

for adj in adjs:
    for n in ns:
        print("{} as {}".format(adj,n))
