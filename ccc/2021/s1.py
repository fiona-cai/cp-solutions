#https://dmoj.ca/problem/ccc21s1
#CCC '21 S1 - Crazy Fencing

n = int(input())

heights = list(map(int, input().split()))
bases = list(map(int, input().split()))


t = 0

for i in range(n):
    h1 = heights[i]
    h2 = heights[i+1]
    b = bases[i]

    a1 = (abs(h1-h2)*b)/2
    a2 = min(h1, h2) * b

    t += a1 + a2


if (t*10) % 10 == 0:

    print(int(t))

else: print(t)
