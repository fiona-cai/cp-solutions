#https://dmoj.ca/problem/ccc16s2
#CCC '16 S2 - Tandem Bicycle

q=int(input())
n=int(input())

dmoj=list(map(int,input().split()))
peg=list(map(int,input().split()))

total=0

dmoj.sort()

if q==1:
    peg.sort()
else:
    peg.sort(reverse=True)

for i in range(n):
    total+= max(dmoj[i],peg[i])

print(total)
