#https://dmoj.ca/problem/ccc20j3
#CCC '20 J3 - Art

ns=[]
ms=[]
a=int(input())
for i in range(a):
    n,m = map(int,input().strip().split(","))
    ns.append(n)
    ms.append(m)

ns.sort()
ms.sort()

print("{},{}".format(ns[0]-1,ms[0]-1))
print("{},{}".format(ns[a-1]+1,ms[a-1]+1))
