#https://dmoj.ca/problem/ccc11s1
#CCC '11 S1 - English or French?

n = int(input())
x = ""
for i in range(n):
    x = x + " " + input().lower()


t = x.count("t")
s = x.count("s")

if t > s: print("English")
else: print("French")
