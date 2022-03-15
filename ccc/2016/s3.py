#https://dmoj.ca/problem/ccc16s3
#CCC '16 S3 - Phonomenal Reviews

from collections import deque
import sys
sys.setrecursionlimit(1000000)

n,m = (int(x) for x in input().split())

restaurants = input().split()
    
graph = [[] for i in range(n)]
included = [False]*n
nodes = 0
start = ...
for i in restaurants:
    start = int(i)
    included[int(i)] = True

def bfs(start):
    q = deque()
    visited = [False]*n
    minSteps = {}
    q.append(start)
    visited[start] = True
    minSteps[start] = 0

    mxd, mxn = 0, -1

    while len(q):
        curr = q.popleft()
        currSteps = minSteps[curr]
        mxd = currSteps
        mxn = curr


        for neighbour in graph[curr]:
            if visited[neighbour] == False:
                if included[neighbour]:
                    visited[neighbour] = True
                    minSteps[neighbour] = currSteps+1
                    q.append(neighbour)

    return [mxd, mxn]
def dfs(curr, vis):
    global nodes
    for neighbour in graph[curr]:
        if neighbour != vis:
            dfs(neighbour, curr)
            if included[neighbour]: included[curr] = True

    if included[curr]: nodes += 1

for i in range(n-1):
    a,b = (int(x) for x in input().split())
    
    graph[a].append(b)
    graph[b].append(a)


dfs(start, -1)

for i in range(n):
    if included[i]:
        break

x = bfs(i)
y = bfs(x[1])

print(2*(nodes-1) - y[0])
