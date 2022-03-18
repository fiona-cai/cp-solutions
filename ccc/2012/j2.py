#https://dmoj.ca/problem/ccc12j2
#CCC '12 J2 - Sounds fishy!

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if d > c > b > a:
    print("Fish Rising")
elif d < c < b < a:
    print("Fish Diving")
elif a == b == c == d:
    print("Fish At Constant Depth")
else:
    print("No Fish")
