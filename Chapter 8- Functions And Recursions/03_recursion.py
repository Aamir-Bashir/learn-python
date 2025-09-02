#Recursion is a function that call itself for example:

def factorial(n):
    if(n==1 or n == 0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter a Number: "))

print(f"The Factorial of this Number is {factorial(n)}")