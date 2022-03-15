#https://dmoj.ca/problem/ccc18j5
#CCC '18 J5 - Choose your own path

def reachable(graph, n):
    queue = [1]
    visited = [False]*(n+1)
    visited[0] = True
    while queue != []:
        curr = queue.pop(0)
        visited[curr] = True
        if curr in graph:
            for neighbour in graph[curr]:
                if visited[neighbour] == False:
                    queue.append(neighbour)

    return False not in visited

def shortestPath(graph, n):
    queue = [1]
    steps = {}
    steps[1] = 1
    totalSteps = -1
    while queue != []:
        curr= queue.pop(0)
        currSteps = steps[curr]

        if curr not in graph:
            totalSteps = currSteps
            break
        for neighbour in graph[curr]:
            if neighbour not in steps:
                queue.append(neighbour)
                steps[neighbour] = currSteps + 1
    
    return totalSteps

n = int(input())
graph = {}
for i in range(1, n+1):
    x= list(map(int, input().split()))
    if x != [0]:
        x.pop(0)
        graph[i] = x



if reachable(graph, n):
    print("Y")
else:
    print("N")

print(shortestPath(graph, n))
