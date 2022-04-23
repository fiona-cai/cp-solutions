#https://dmoj.ca/problem/rgpc18p3
#RGPC '18 P3 - Chocolate Day

n, t = map(int, input().split())

psa = [0] * (n+2)
dif = [0] * (n+2)

for i in range(t):
    a, b, c = map(int, input().split())
    dif[a] += c
    dif[b + 1] -= c

L = 1
l = int(input())

best = 0
for R in range(1, n + 1):
    dif[R] += dif[R - 1]
    psa[R] = psa[R - 1] + dif[R]
    while psa[R] - psa[L - 1] > l:
        L += 1
    
    best = max(best, R - L + 1)

print(best)
