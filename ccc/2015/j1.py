#https://dmoj.ca/problem/ccc15j1
#CCC '15 J1 - Special Day

m = int(input())
d = int(input())

if m < 2:
    print("Before")
elif m > 2:
    print("After")
else:
    if d < 18:
        print("Before")
    elif d == 18:
        print("Special")
    else:
        print("After")
