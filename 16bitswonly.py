#https://dmoj.ca/problem/16bitswonly
#16 BIT S/W ONLY

for _ in range(int(input())):
    a,b,p = map(int,input().split())
    if a*b == p:
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")
