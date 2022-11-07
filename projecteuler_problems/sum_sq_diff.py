# quick program to take the difference between
#the square of the sum of the first ten natural numbers
# and sum of the squares of the first ten natural numbers.


n=int(input('Enter number to be summed, squared and subtracted: '))

def Sum_sq_diff(n):
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) / 6
    Sq_of_sum = ((n * (n + 1)) / 2) ** (2)
    return Sq_of_sum-sum_of_squares

print(Sum_sq_diff(n))



