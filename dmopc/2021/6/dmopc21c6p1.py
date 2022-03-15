#https://dmoj.ca/problem/dmopc21c6p1
#DMOPC '21 Contest 6 P1 - Bigger Big Integer

d=int(input())
x=list(input())
for i in range(d-1):
  if x[i] < x[i+1]:
    temp=x[i]
    x[i]=x[i+1]
    x[i+1]=temp
    break

print(*x,sep="")
