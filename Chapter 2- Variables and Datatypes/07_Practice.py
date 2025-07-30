#Problem 1 : Add two numbers
a = 10
b = 20
sum = a + b
print("Sum of a and b is:", sum)            

#Problem 2 : Write a python ptogram to find remainder when a number is divided by another number
c = 10
d = 3
remainder = c % d
print("Remainder when", c, "is divided by", d, "is:", remainder)

#Problem 3 : Write a python program to find the type of a variable using input () fumction4
e = input("Enter a number: ")
print("The type of the variable is:", type(a))  # This will show <class 'str'> since input() returns a string

# Problem 4 : Use comparison operators to find out whether a given number is a greater than 'g' or not.
f = int(input("Enter a number: "))
g = int(input("Enter another number: "))

print("f is greater than g:", f > g)  # This will compare the two numbers and print True or False

# Problem 5 : Write a python program to find the Average of two numbers

h = int(input("Enter first number: "))
i = int(input("Enter second number: "))

avg = ( h + i)/2

print("The average of", h, "and", i, "is:", avg)

# Problem 6 : Write a python program to calculate the square of entered number by user
j = int(input("Enter a number to find its square: "))
sq = j**2
print("The square of", j , "is: ", sq)