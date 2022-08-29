#https://dmoj.ca/problem/dmopc13c3p2
#DMOPC '13 Contest 3 P2 - Phone Microwave

M = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

s = int(input())
a, b = map(str,input().split())
y, m, d = map(int, a.split("/"))
h, min, sec = map(int, b.split(":"))
c = m - 2
d += ((h - s)-(h - s)%24)//24
h = (h - s)%24

while True:
    if d <= 0:
        d += M[c%12]
        if m == 1:
            y -= 1
            m = 12
        else:
            m -= 1
        c -= 1
    else:
        break

def zero(x):
    if len(str(x)) == 1:
        x = "0{}".format(x)
    return x

print("{}/{}/{} {}:{}:{}".format(zero(y), zero(m), zero(d), zero(h), zero(min), zero(sec)))
