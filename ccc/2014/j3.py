#https://dmoj.ca/problem/ccc14j3
#CCC '14 J3 - Double Dice

r = int(input())
a = 0
d = 0
while r > 0:
    y = input()
    x = list(y)
    for i in x:
        if i == " ":
            x.remove(i)
    r -= 1
    if x[0] > x[1]:
        d += int(x[0])
    elif x[0] < x[1]:
        a += int(x[1])

print(100-a)
print(100-d)
