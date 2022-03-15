#https://dmoj.ca/problem/dmopc17c5p2
#DMOPC '17 Contest 5 P2 - Mimi and Binary

import bisect
s=list(map(int,input()))
q=int(input())
psa1=[0]
psa0=[0]
c1=0
c0=0
for i in s:
    if i==0:
        c0+=1
    psa0.append(c0)

for i in s:
    if i==1:
        c1+=1
    psa1.append(c1)

for _ in range(q):
    x,y,z=map(int,input().split())
    if z==0:
        ans=(bisect.bisect_left(psa0,y+psa0[x-1]))
        
    else:
        ans=(bisect.bisect_left(psa1,y+psa1[x-1]))

    if ans>len(s):
        print(-1)
    else:
        print(ans)
