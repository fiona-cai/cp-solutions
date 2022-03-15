#https://dmoj.ca/problem/ccc17j3
#CCC '17 J3 - Exactly Electrical

a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))
t=int(input())

sum = abs(a-c)+abs(b-d)
if sum<=t:
    if sum%2:
        if t%2:
            print("Y")
        else:
            print("N")
    else:
        if not t%2:
            print("Y")
        else:
            print("N")
else:
    print("N")
