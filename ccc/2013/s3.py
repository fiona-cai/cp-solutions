#https://dmoj.ca/problem/ccc13s3
#CCC '13 S3 - Chances of Winning

def score(i):
    if i == len(game):
        for i in range(4):
            if i != t and points[i] >= points[t]:
                return 0
        return 1
    
    ways = 0
    a, b = game[i]

    points[a] += 3
    ways += score(i+1)
    points[a] -= 3

    points[b] += 3
    ways += score(i+1)
    points[b] -= 3

    points[a] += 1
    points[b] += 1
    ways += score(i+1)
    points[a] -= 1
    points[b] -= 1

    return ways

t = int(input()) - 1
g = int(input())

points = [0]*4
game = [(0,1), (0,2), (0,3), (1, 3), (1, 2), (2, 3)]

for _ in range(g):
    a,b, sa, sb = (int(x) for x in input().split())
    a -= 1
    b -= 1
    if sa > sb:
        points[a] += 3
    elif sb > sa:
        points[b] += 3
    else:
        points[a] += 1
        points[b] += 1
    game.remove((a,b))

print(score(0))
