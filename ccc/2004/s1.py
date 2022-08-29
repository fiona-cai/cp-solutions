#https://dmoj.ca/problem/ccc04s1
#CCC '04 S1 - Fix

n=int(input())
for _ in range(n):
    s=[]
    for i in range(3):
        s.append(input().strip())
    fixfree=True
    for i in range(3):
        for j in range(3):
            if i==j:
                continue
            if(s[i].startswith(s[j]) or s[i].endswith(s[j])):
                fixfree=False
    if fixfree:
        print("Yes")
    else:
        print('No')
