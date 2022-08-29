#https://dmoj.ca/problem/pulse
#Pulse

n,s,t=map(int,input().split())
c=0
for i in range(n):
    if s <= int(input())*2 <= t:
        c+=1

print(c)
