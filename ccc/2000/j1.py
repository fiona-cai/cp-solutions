#https://dmoj.ca/problem/ccc00j1
#CCC '00 J1 - Calendar

start,total=map(int,input().split())
day=start
print("Sun Mon Tue Wed Thr Fri Sat")

for i in range(start-1):
    print("   ",end="")

for i in range(start-2):
    print(" ",end="")

for i in range(1,total+1):
    if day==1:
        print(str(i).rjust(3),end="")
    else:
        print(str(i).rjust(4),end="")
    day+=1
    if day>7:
        print()
        day=1

if not day==1:
    print()
