#https://dmoj.ca/problem/ccc18s1
#CCC '18 S1 - Voronoi Villages

n = int(input())

v = []

for i in range(n):
    v.append(int(input()))

v.sort()


min = 9999999999999999999999999

for i in range(len(v)):
    if i != 0 and i != len(v)-1:
        c = v[i]
        size = (c - ((c + v[i-1])/2)) + (((v[i+1] + c)/2) - c)

        if (size < min):
            min = size

print(float(min))
