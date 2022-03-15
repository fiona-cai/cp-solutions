#https://dmoj.ca/problem/dmopc17c2p2
#DMOPC '17 Contest 2 P2 - Balance

s=input()
val = 0
nmin = 1000000
for i in s:
    if i=="(":
        val+=1
    else:
        val-=1
    nmin=min(nmin,val)

if (val==0 and nmin>=0)or (val==-2 and nmin>=-2) or(val==2 and nmin>=0):
    print("YES")
else:
    print("NO")
