#https://dmoj.ca/problem/ccc20j2
#CCC '20 J2 - Epidemiology

p=int(input())
n=int(input())
r=int(input())
c = 0
total = n
while total<=p:
    n*=r
    total+=n
    c+=1

print(c)
