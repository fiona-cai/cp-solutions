#https://dmoj.ca/problem/ccc17j2
#CCC '17 J2 - Shifty Sum

n = int(input())
k = int(input())
sum = n
for _ in range(k):
    n*=10
    sum+=n

print(sum)
