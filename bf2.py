#https://dmoj.ca/problem/bf2
#Lexicographically Least Substring

s=input()
k=int(input())
combos=[]

x = s[:k]
mn = x

for i in range(k, len(s)):
    x = x[1:k] + s[i] 
    if x < mn:
        mn = x

print(mn)
