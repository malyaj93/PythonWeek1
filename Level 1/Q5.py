# Writing function to calculate factorial using for loop

def factorial(num):
    res = 1
    for i in range(2, num + 1):
        res *= i
    return res

n = int(input("Enter a number: "))
fact = factorial(n)
print("Factorial of n is : ", fact)