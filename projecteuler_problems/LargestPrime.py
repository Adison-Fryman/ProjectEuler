
import math
input = input('Enter number to be factored here: ')
number = int(input)
prime_factors_of_number=[]

def factor_finder(number):
    factors = []
    for x in range(1,int(math.sqrt(number))+1):
        if number % x == 0:
            factors.append(x)
    factors.append(number)
    return factors

factors_of_number = factor_finder(number)


#(prime numbers should only have two factors, 1 and themselves)
for factor in factors_of_number:
    if len(factor_finder(factor)) ==2:
        prime_factors_of_number.append(factor)



print(prime_factors_of_number[-1])
