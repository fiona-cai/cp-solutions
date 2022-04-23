#https://dmoj.ca/problem/bf1hard
#List Minimum (Hard)

a = int(input())
el = []

for i in range(0, a): 
    ele = int(input()) 
    el.append(ele)

el.sort()

print(*el, sep = "\n")
