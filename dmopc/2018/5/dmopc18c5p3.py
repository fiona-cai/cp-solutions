#https://dmoj.ca/problem/dmopc18c5p3
#DMOPC '18 Contest 5 P3 - A Familiar Problem

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
line = list(map(int, input().split()))
psa = [0]
for i in range(1, len(line) + 1):
    psa.append(line[i - 1] + psa[i - 1])
l, r, ans = 1, 1, 0
while r <= n:
    while psa[r] - psa[l-1] >= m :
        l += 1
    ans = max(ans, r - l + 1)
    r += 1
print(ans)
