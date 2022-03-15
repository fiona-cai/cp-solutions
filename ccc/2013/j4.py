#https://dmoj.ca/problem/ccc13j4
#CCC '13 J4 - Time on task

total = 0
ans = 0
chores = []

time = int(input())
aofc = int(input())
for i in range(aofc):
    chores.append(int(input()))

chores.sort()

for i in chores:
    total += i
    ans += 1
    if total > time:
        total -= i
        ans -= 1

print(ans)
