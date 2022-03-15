#https://dmoj.ca/problem/dmopc21c6p2
#DMOPC '21 Contest 6 P2 - Gacha Luck

n,k=map(int,input().split())
entries=list(map(str,input().split("1")))
entries.sort(key=len)
total=0
for i in range(1,k+1):
   try:
      total+=len(entries[-i])
   except Exception:
      break
print(total)
