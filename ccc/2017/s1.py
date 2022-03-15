#https://dmoj.ca/problem/ccc17s1
#CCC '17 S1 - Sum Game

n = int(input())
swift = list(map(int, input().split()))
sema = list(map(int, input().split()))

swifts = 0
semas = 0
maxs = 0


for d in range(0, n):
    swifts += swift[d]
    semas += sema[d]
    if swifts == semas:
        maxs = d+1
                
print(maxs)
