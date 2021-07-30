# GET ANY FIBONACCI

# First we assign the nth_Fibonacci variable the nth Fibonacci number
# to-be-calculated. The nth number 42 is used as an example, which has
# a Fibonacci value of 267914296.

nth_Fibonacci = 42

# In the Fibonacci sequence, the nth number is the sum of the two previous
# numbers, or n-1 and n-2. To calculate the nth number, a seed Array variable
# is populated with the value of nth_Fibonacci, both values added accordingly,
# and then exported.


def Fibonacci(n):

    Array = [0, 1]

    for i in range(2, n):
        Array.append(Array[i-1] + Array[i-2])
    return Array[n-1]


# Finally, the value of the nth number is printed.

answer = Fibonacci(nth_Fibonacci+1)

print(answer)
