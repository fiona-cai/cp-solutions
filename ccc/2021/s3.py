#https://dmoj.ca/problem/ccc21s3
#CCC '21 S3 - Lunch Concert

import sys
input = sys.stdin.readline

n = int(input())

friends = []
for _ in range(n):
    p,w,d = (int(x) for x in input().split())
    friends.append([p,w,d])


def dist(pos):
    sum = 0
    for i in range(n):
        p,w,d = friends[i]
        if p == pos:
           continue
        elif p > pos:
            p -= d
            p = max(pos, p)
            sum += abs(p-pos)*w
        else:
            p += d
            p = min(p,pos)
            sum += abs(p-pos)*w
    return sum

lastsum = 999999999999999

low = 0
high = int(1e9)

while low < high:
    mid = (low+high)//2
    curr, curr1 = dist(mid), dist(mid+1)

    if curr > curr1:
        low = mid+1
    else:
        high = mid

print(dist(low))
