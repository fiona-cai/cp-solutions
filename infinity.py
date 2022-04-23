#https://dmoj.ca/problem/infinity
#Infinity

a=(input())
b=(input())

sum = int(hex(int(a, 16) + int(b, 16)),16)
if sum>int("3F3F3F3F",16):
    print("Yes")
else:
    print("No")
