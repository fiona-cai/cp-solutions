#https://dmoj.ca/problem/ccc03j1
#CCC '03 J1 - Trident

t=int(input())
s=int(input())
h=int(input())

row="*{x}*{x}*".format(x=" "*s)
for i in range(t):
    print(row)

print("*{x}*{x}*".format(x="*"*s))

row="{}*".format(" "*(s+1))

for i in range(h):
    print(row)
