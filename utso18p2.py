#https://dmoj.ca/problem/utso18p2
#UTS Open '18 P2 - ABCs

import sys

input=sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

m = 0
if b[0] == a[2] and c[0] > 0:
    m += c[0]
if b[1] == a[0] and c[1] > 0:
    m += c[1]
if b[2] == a[1] and c[2] > 0:
    m += c[2]
print(m)
