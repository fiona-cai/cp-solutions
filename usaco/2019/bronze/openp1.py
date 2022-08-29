#https://dmoj.ca/problem/usaco19openbronze1
#USACO 2019 Open Contest Bronze P1 - Bucket Brigade

from collections import deque
grid = []

for _ in range(10):
    i = input()
    grid.append(i)

    try:
        lakepos = [_, i.index("L")]  
    except ValueError: 
        __ = 0
    try:
        barnpos = [_, i.index("B")]
    except ValueError:
        continue

nextpos = [(1,0), (0,1), (-1, 0), (0,-1)]

q = deque()
minSteps = [[False for i in range(10)] for j in range(10)]

q.append(lakepos)
x,y = lakepos[0], lakepos[1]
minSteps[x][y] = 0

while len(q):
    currx, curry = q.popleft()
    currSteps = minSteps[currx][curry]
    if [currx, curry] == barnpos:
        break

    for nx, ny in nextpos:
        nextx, nexty = currx+nx, curry+ny
        if 0 <= nextx < 10 and 0 <= nexty < 10:
            if minSteps[nextx][nexty] == False:
                if grid[nextx][nexty] != "R":
                    q.append([nextx, nexty])
                    minSteps[nextx][nexty] = currSteps+1

print(minSteps[barnpos[0]][barnpos[1]] - 1)
