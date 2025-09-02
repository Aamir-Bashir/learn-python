#Write a program to calculate Factorial of given number using for loop

n = int(input("Enter a Number: ")) 
product = 1

for i in range(1,n+1):
    product = product * i
print(f"The Factorial of {n} is {product}")