#https://dmoj.ca/problem/ccc20j1
#CCC '20 J1 - Dog Treats

s=int(input())
m=int(input())
l=int(input())

if(s+2*m+3*l)<10:
    print("sad")
else:
    print("happy")
