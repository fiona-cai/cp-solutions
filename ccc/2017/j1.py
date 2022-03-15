#https://dmoj.ca/problem/ccc17j1
#CCC '17 J1 - Quadrant Selection

x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)
