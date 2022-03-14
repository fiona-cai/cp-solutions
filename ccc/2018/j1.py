#https://dmoj.ca/problem/ccc18j1
#CCC '18 J1 - Telemarketer or not?

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a in (9, 8):
    if d in (8, 9):
        if b == c:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
