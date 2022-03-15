#https://dmoj.ca/problem/usaco19febb2
#USACO 2019 February Bronze P2 - The Great Revegetation

n, m = map(int, input().split())
pastures = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    pastures[a].append(i)
    pastures[b].append(i)

GrassTypeToCows = [set() for i in range(n+1)]
types = ""
for pasture in range(1, n+1):
    if pasture == 0:
        types = "1"
        for j in pastures[pasture]:
            GrassTypeToCows[pasture].add(j)
    else:
        for type in range(1, 5):
            work = True
            for reliantCow in pastures[pasture]:
                if reliantCow in GrassTypeToCows[type]:
                    work = False
                    break
            if work:
                types = types + str(type)
                for reliantCow in pastures[pasture]:
                    GrassTypeToCows[type].add(reliantCow)
                break

print(types)
