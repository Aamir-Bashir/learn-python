#write a program to print a table of a given number using while loop

num = int(input("Enter a Number: "))
i = 1
while(i<11):
    print(f"{num} x {i} ={num*i} ")
    i += 1