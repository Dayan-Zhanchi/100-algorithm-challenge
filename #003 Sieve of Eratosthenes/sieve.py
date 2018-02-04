import sys
import math

def sieve(n):
    a = []
    for i in range(n+1):
        a.append(True)
    
    for i in range(2,int(math.sqrt(n+1))):
        if a[i]:
            j = i*i
            while j <= n:
                a[j] = False
                j +=i
    
    return a

def main():
    n = int(sys.argv[1])
    a = sieve(n)
    primes = []
    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
    print(primes)

if __name__=="__main__":
    main()