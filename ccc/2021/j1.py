#https://dmoj.ca/problem/ccc21j1
#CCC '21 J1 - Boiling Water

b=int(input())
p=5*b-400
print(p)

if p==100:
    print(0)
elif p<100:
    print(1)
else:
    print(-1)
