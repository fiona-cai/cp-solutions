#https://dmoj.ca/problem/ccc04j2
#CCC '04 J2 - Terms of Office

x = int(input())
y = int(input())

for i in range(x, y + 1):
    if (i - x) % 60 == 0:
        print("All positions change in year {}".format(i))
