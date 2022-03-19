#CCC '12 J3 - Icon Scaling
#https://dmoj.ca/problem/ccc12j3

k = int(input())

for i in range(k):
    print("*"*k +"x" *k+ "*" *k)

for i in range(k):

    print(" "*k + "x" *(k+k))

for i in range(k):
    print("*"*k + " "*k + "*"*k)
