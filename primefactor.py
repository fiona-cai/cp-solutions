#https://dmoj.ca/problem/primefactor
#Prime Factorization

def primef(n):
    i = 2
    f = []
    while i**2 <= n:
        if n % i:
            i += 1
        else:
            n = int(n/i)
            f.append(i)
    if n > 1:
        f.append(n)
    return f
    
for _ in range(int(input())):
  n = int(input())
  print(*primef(n))
