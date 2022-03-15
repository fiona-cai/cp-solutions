#https://dmoj.ca/problem/ccc18s3
#CCC '18 S3 - RoboThieves

import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
grid = []
spos = []
nextpos = [(0,1), (1,0), (0,-1), (-1, 0)]
invalid = set()
cameras = []


for _ in range(n):
    x = input()
    grid.append(x)
    try: spos = (_, x.index("S")) 
    except ValueError: nn = 1
    for i in range(m):
        if x[i] == "C":
            cameras.append([_, i])

for x, y in cameras:
    prev = {}
    visited = [[False for i in range(m)]for j in range(n)]
    q = deque()
    prev[(x,y)] = "A"
    q.append([x,y])
    visited[x][y] = True
    while len(q):
        curr = q.popleft()

        for nx, ny in nextpos:
            nextx, nexty = curr[0]+nx, curr[1]+ny
            if 0 <= nextx < n and 0 <= nexty < m:
                if visited[nextx][nexty] == False:
                    if grid[nextx][nexty] != "W":
                        if prev[(curr[0],curr[1])] == (nx, ny) or prev[(curr[0],curr[1])] == "A":
                            visited[nextx][nexty] = True
                            q.append([nextx, nexty])
                            prev[(nextx, nexty)] = (nx, ny)
                            if grid[nextx][nexty] == "." or grid[nextx][nexty] == "S":
                                invalid.add((nextx, nexty))


q = deque()
visited = [[False for i in range(m)]for j in range(n)]
minSteps = {}
minSteps[spos] = 0
q.append(spos)
visited[spos[0]][spos[1]] = True
conveyormoves = deque()
while len(q):
    curr = q.popleft()
    currSteps = minSteps[(curr[0], curr[1])]
    if len(conveyormoves) == 0: nextmove = [0, 0]
    else: nextmove = conveyormoves.popleft()

    if nextmove == [0,0]:
        for nx, ny in nextpos:
            nextx, nexty = curr[0]+nx, curr[1]+ny
            if 0 <= nextx < n and 0 <= nexty < m:
                if visited[nextx][nexty] == False:
                    if grid[nextx][nexty] != "W" and grid[nextx][nexty] != "C":
                        if grid[nextx][nexty] == ".":
                            if (nextx, nexty) in invalid: continue
                            conveyormoves.append([0,0])
                            visited[nextx][nexty] = True
                            q.append([nextx, nexty])
                            minSteps[(nextx, nexty)] = currSteps + 1
                        else:
                            if grid[nextx][nexty] == "U": conveyormoves.insert(0, (-1, 0))
                            elif grid[nextx][nexty] == "L": conveyormoves.insert(0, (0, -1))
                            elif grid[nextx][nexty] == "R": conveyormoves.insert(0, (0, 1))
                            else: conveyormoves.insert(0, (1, 0))
                            visited[nextx][nexty] = True
                            q.insert(0, [nextx, nexty])
                            minSteps[(nextx, nexty)] = currSteps + 1
                        
    else:
        nextx, nexty = curr[0]+nextmove[0], curr[1]+nextmove[1]
        if not visited[nextx][nexty]:
            if grid[nextx][nexty] == "W" or grid[nextx][nexty] == "C": continue
            if grid[nextx][nexty] == ".":
                if (nextx, nexty) in invalid: continue
                conveyormoves.append([0,0])
                visited[nextx][nexty] = True
                q.append([nextx, nexty])
                minSteps[(nextx, nexty)] = currSteps
            else:
                if grid[nextx][nexty] == "U": conveyormoves.insert(0, (-1, 0))
                elif grid[nextx][nexty] == "L": conveyormoves.insert(0, (0, -1))
                elif grid[nextx][nexty] == "R": conveyormoves.insert(0, (0, 1))
                else: conveyormoves.insert(0, (1, 0))
                q.insert(0, [nextx, nexty])
                minSteps[(nextx, nexty)] = currSteps
                visited[nextx][nexty] = True
            

for i in range(n):
    for j in range(m):
        if grid[i][j] == ".":
            if spos in invalid: print(-1); continue
            if (i, j) in minSteps:
                print(minSteps[(i, j)])
            else: print(-1)
