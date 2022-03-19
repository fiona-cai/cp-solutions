#CCC '12 S1 - Don't pass me the ball!
#https://dmoj.ca/problem/ccc12s1

j = int(input())
cnt = 0
for f in range(1, j):
    for s in range(f+1, j):
        for t in range(s+1, j):
            cnt += 1

print(cnt)
