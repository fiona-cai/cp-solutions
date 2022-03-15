#https://dmoj.ca/problem/dmopc21c5p1
#DMOPC '21 Contest 5 P1 - Permutations & Primes

n=int(input())

if n==1:
    print(1)
elif n<=4:
    print(-1)
else:
    odd=list(range(1,n+1,2))
    even=list(range(2,n+1,2))
    odd.remove(5)
    even.remove(4)
    print(*odd,5,4,*even)
