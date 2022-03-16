#https://dmoj.ca/problem/ccc02j1
#CCC '02 J1 - 0123456789

n=int(input())

h=" * * *"
v0="*\n*\n*"
v2="      *\n      *\n      *"
v02="*     *\n*     *\n*     *"

if n==1:
    print()
    print(v2)
    print()
    print(v2)
    print()

elif n==2:
    print(h)
    print(v2)
    print(h)
    print(v0)
    print(h)

elif n==3:
    print(h)
    print(v2)
    print(h)
    print(v2)
    print(h)

elif n==4:
    print()
    print(v02)
    print(h)
    print(v2)
    print()

elif n==5:
    print(h)
    print(v0)
    print(h)
    print(v2)
    print(h)

elif n==6:
    print(h)
    print(v0)
    print(h)
    print(v02)
    print(h)

elif n==7:
    print(h)
    print(v2)
    print()
    print(v2)
    print()

elif n==8:
    print(h)
    print(v02)
    print(h)
    print(v02)
    print(h)

elif n==9:
    print(h)
    print(v02)
    print(h)
    print(v2)
    print(h)

elif n==0:
    print(h)
    print(v02)
    print()
    print(v02)
    print(h)
