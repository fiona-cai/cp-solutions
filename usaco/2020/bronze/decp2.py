#https://dmoj.ca/problem/usaco20decb2
#USACO 2020 December Bronze P2- Daisy Chains

n = int(input())

petals = list(map(int, input().split()))
cnt = 0
for i in range(n):
    for j in range(i+1, n):
        newlist = petals[i:j+1]
        if sum(newlist)/len(newlist) in newlist:
            cnt += 1

print(cnt+n)
