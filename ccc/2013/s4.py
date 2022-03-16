#https://dmoj.ca/problem/ccc13s4
#CCC '13 S4 - Who is Taller?

import sys
input = sys.stdin.readline
from collections import deque

def checkReachable(p, q, heights):
    visited = [False]*(n+1)
    queue = deque()
    queue.append(p)
    visited[p] = True
    while len(queue):
        curr = queue.popleft()
        if curr == q:
            return True
        if curr in heights:
            for neighbour in heights[curr]:
                if visited[neighbour] == False:
                    queue.append(neighbour)
                    visited[neighbour] = True
    
    return False



n,m = (int(x) for x in input().split())
heights = {}

for i in range(m):
    x, y = (int(x) for x in input().split())
    if x in heights:
        heights[x].append(y)

    else:
        heights[x] = [y]
p, q = (int(x) for x in input().split())

if checkReachable(p, q, heights):
    print("yes")
elif checkReachable(q, p, heights):
    print("no")
else:
    print("unknown")
