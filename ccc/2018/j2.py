#https://dmoj.ca/problem/ccc18j2
#CCC '18 J2 - Occupy parking

N = int(input())
y = input()
t = input()

x = 0

list(y)
list(t)

for a, b in zip(y, t):
    if a == b == "C":
        x += 1
      
print(x)
