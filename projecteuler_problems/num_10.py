# how to generate prime numbers
#

from math import isqrt

n=2000000
def primes_less_than(n):
    if n<=2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2,n):
            if is_prime[i]:
                for x in range(i*i,n,i):
                    is_prime[x] = False

    return [i for i in range(n) if is_prime[i]]


list_of_primes=primes_less_than(n)
#print(list_of_primes)
print(sum(list_of_primes))