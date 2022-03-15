#https://dmoj.ca/problem/dmopc20c5p1
#DMOPC '20 Contest 5 P1 - Home Row

ss = list(input())
ts = list(input())
index = 0
count = 0
for s,t in zip(ss,ts):
    if s == t:
        index += 1
    else:
        break
for s in ss[index:]:
    ss.pop()
    count += 1
for t in ts[index:]:
    ss.append(t)
    count += 1

print(count)
