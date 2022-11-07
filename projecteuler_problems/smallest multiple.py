#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

smallest= []
given_list= range(1,20)

for x in range(1,10000):
    for y in range(1,20):
        if x%y == 0:
            smallest.append(x)
   # result_true = all(num % x==0 in given_list)
  #  if result_true==True:


print(smallest)
###
real solution
import math

print(math.lcm(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20))

print(1*2*3*5*7*2*2*3*11*13*2*17*19)
