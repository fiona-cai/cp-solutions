#only works when submitted with python 2
#https://dmoj.ca/problem/dmopc21c7p1
#DMOPC '21 Contest 7 P1 - Chika Grids

import sys

n,m=map(int,input().split())
rows=[[0]*(m+2)]
for i in range(n):
    row=list(map(int,input().split()))
    row.insert(0,0)
    row.append(0)
    rows.append(row)
rows.append([0]*(m+2))
for r in range(1,n+1):
    for c in range(1,m+1):
        if rows[r][c] == 0:
            num=rows[r][c-1]+1
            while True:
                if num>rows[r][c-1] and num>rows[r-1][c]:
                    rows[r][c] = num
                    break
                num+=1
        else:
            if not (rows[r][c]>rows[r][c-1] and rows[r][c]>rows[r-1][c]):
                print(-1)
                sys.exit()

for row in range(1,n+1):
    rows[row].pop(0)
    rows[row].pop(-1)
    print(*rows[row])
