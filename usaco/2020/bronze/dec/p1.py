#https://dmoj.ca/problem/usaco20decb1
#USACO 2020 December Bronze P1 - Do You Know Your ABCs?

def checkPerm(i, totalsum):
    a = i[0]
    b = i[1]
    c = i[2]
    d = i[3]
    e = i[4]
    f = i[5]

    return a + b == d and b+c == e and a+c == f and a+b+c == totalsum

from itertools import permutations

nums = list(map(int, input().split()))
totalsum = max(nums)
nums.remove(totalsum)

perms = permutations(nums)

for i in perms:
    if checkPerm(i, totalsum):
        l = [i[0], i[1], i[2]]
        l.sort()
        print(l[0], l[1], l[2])
        break
