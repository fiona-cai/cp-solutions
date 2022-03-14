#https://dmoj.ca/problem/ccc19s1
#CCC '19 S1 - Flipper

og = [[1, 2], [3, 4]]

c = input()

for i in range(len(c)):
    if c[i] == 'H':
        og[0][0], og[1][0] = og[1][0], og[0][0]
        og[0][1], og[1][1] = og[1][1], og[0][1]
    else:
        og[0][0], og[0][1] = og[0][1], og[0][0]
        og[1][0], og[1][1] = og[1][1], og[1][0]

print(og[0][0], og[0][1])
print(og[1][0], og[1][1])
