#Write a proram to print a table in reverse order using for loop

n = int(input("Enter a Number: "))

for i in range(1,11):
    print(f"{n} x {11-i} = {n * (11-i)}")