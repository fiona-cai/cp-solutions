#https://dmoj.ca/problem/dmopc19c2p1
#DMOPC '19 Contest 2 P1 - Box and Whiskers

import statistics

n=int(input())
nas=list(map(int,input().split()))
nas.sort()
ans=[nas[0],nas[-1],0,statistics.median(nas),0]
ans[2]=statistics.median(nas[:n//2])
ans[4]=statistics.median(nas[((n-1)//2)+1:])

print(*ans,sep=" ")
