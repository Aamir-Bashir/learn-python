# A Python function is a named, reusable block of code designed to perform a specific task.
'''
a = int(input("Enter a Number: "))
b = int(input("Enter a Number: "))
c = int(input("Enter a Number: "))
average = (a + b + c)/3
to print this 50 times we need re write the whole lines of code again and again
so here comes the functions
'''
#For Example

#Function Definition
def avg():
    a = int(input("Enter a Number: "))
    b = int(input("Enter a Number: "))
    c = int(input("Enter a Number: "))
    average = (a + b + c)/3
    print(average)

#We will call the function like this and we can call it as many times as we want to make it work
avg()
avg()
avg()
avg()
avg()