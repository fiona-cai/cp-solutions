#https://dmoj.ca/problem/usaco19febs1
#USACO 2019 February Silver P1 - Sleepy Cow Herding

a = []

def findMin():
    if a[n-2]-a[0] == n-2 and a[n-1] - a[n-2] > 2: return 2
    if a[n-1]-a[1] == n-2 and a[1]-a[0]>2: return 2
    j = 0
    best = 0
    for i in range(n): 
        while j<n-1 and a[j+1]-a[i]<=n-1:
            j += 1
        best = max(best, j-i+1)
    
    return n-best

 
n = int(input())
for i in range(n): a.append(int(input())) 
a.sort()

answer_min = findMin()
answer_max = max(a[n-2]-a[0], a[n-1]-a[1]) - (n-2)
print(answer_min)
print(answer_max)
