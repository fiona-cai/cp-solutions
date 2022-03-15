#https://dmoj.ca/problem/ccc20s1
#CCC '20 S1 - Surmising a Sprinter's Speed

n = int(input())
m = []

for i in range(n):
    a, b = (int(x) for x in input().split())
    m.append([a, b])

m.sort(key=lambda e : e[0])

max = 0

for i in range(len(m)-1):
    pos2 = m[i+1][1]
    pos1 = m[i][1]
    t2 = m[i+1][0]
    t1 = m[i][0]
    speed = abs((pos2-pos1)/(t2-t1))
    if speed > max:
        max = speed

print(max)
