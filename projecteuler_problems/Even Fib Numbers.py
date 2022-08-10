#Fibonacci even numbers sum for less than 4,000,000.
Fibonacci_all = [1,2]
Fibonacci_even=[]

for x in range(2,100):

    b=Fibonacci_all[(x - 1)]
    c = Fibonacci_all[(x - 2)]
    a = b+c
    Fibonacci_all.append(a)


for num in Fibonacci_all:
    if (num%2==0) and num<4000000:
        Fibonacci_even.append(num)


print(Fibonacci_even)
print(sum(Fibonacci_even))

