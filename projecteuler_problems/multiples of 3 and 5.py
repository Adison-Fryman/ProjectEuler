#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# #we get 3, 5, 6 and 9. The sum of these multiples is 23.
import time

Import time
#Find the sum of all the multiples of 3 or 5 below 1000.
mults_of_3_n_5 = []
removed_dups= []
total_sum=0
for num in range(0,1000):
    if num % 3 == 0:
        mults_of_3_n_5.append(num)
    if num  % 5 == 0:
        mults_of_3_n_5.append(num)
mults_of_3_n_5.sort()

[removed_dups.append(num) for num in mults_of_3_n_5 if num not in removed_dups]

for num in removed_dups:
 total_sum+=num
print(total_sum)


time.sleep(5)

print('thank you for waiting... :)')