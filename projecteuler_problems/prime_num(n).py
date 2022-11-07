# how to generate prime numbers
# tell the prime number at location (a) in a list.

from math import isqrt
a = int(input('At which index do you want the prime number from in the list? '))
n=1000000
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
print(list_of_primes[a-1])

