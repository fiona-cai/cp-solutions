#https://dmoj.ca/problem/ccc19s2
#CCC '19 S2 - Pretty Average Primes

t=int(input())
def isPrime(n):
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

for _ in range(t):
    n= int(input())
    a=3
    b=n*2-a
    while not(isPrime(a) and isPrime(b)):
        a+=2
        b-=2
    print(a,b)
