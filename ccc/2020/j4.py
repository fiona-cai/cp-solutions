#https://dmoj.ca/problem/ccc20j4
#CCC '20 J4 - Cyclic Shifts

t = input()
s = input()
flag = False
for i in range(len(s)):
    if not t.find(s[i:]+s[:i]) == -1:
        flag=True
        break

if flag:
    print("yes")
else:
    print("no")
