#https://dmoj.ca/problem/dmopc20c4p1
#DMOPC '20 Contest 4 P1 - Missing Numbers

n=int(input())

for i in range(n):
    c=0
    n,s=map(int,input().split())
    diff=((n*(n+1))//2)-s

    print((min(n,diff-1))-(diff//2))
