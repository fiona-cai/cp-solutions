#https://dmoj.ca/problem/usaco19openbronze2
#USACO 2019 Open Contest Bronze P2 - Milk Factory

from collections import deque
n = int(input())
graph = {}

def bfs(start):
    q = deque()
    visited = [False]*(n)
    q.append(start)
    visited[start-1] = True
    
    while len(q):
        curr = q.popleft()

        if curr in graph:
            for neighbour in graph[curr]:
                if visited[neighbour-1] == False:
                    visited[neighbour-1] = True
                    q.append(neighbour)
    return False in visited

for _ in range(n-1):
    b,a = (int(x) for x in input().split())
    
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

work = False
for i in range(1, n+1):
    if bfs(i) == False:
        print(i)
        work = True
        break

if not work:
    print(-1)
