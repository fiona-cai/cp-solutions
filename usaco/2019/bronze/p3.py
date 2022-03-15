#https://dmoj.ca/problem/usaco19decbronze3
#USACO 2019 December Bronze P3 - Livestock Lineup

from itertools import permutations

l = ["Beatrice", "Belinda", "Bella", "Bessie", "Betsy", "Blue","Buttercup", "Sue"]
x = permutations(l)

n = int(input())
restrictions = []

for _ in range(n):
    i = input().split()
    restrictions.append([i[0], i[-1]])


for i in x:
    work = True
    for j in restrictions:
        if abs(i.index(j[0]) - i.index(j[1])) != 1:
            work = False
            break
    if work:
        for i2 in i:
            print(i2)
        break
