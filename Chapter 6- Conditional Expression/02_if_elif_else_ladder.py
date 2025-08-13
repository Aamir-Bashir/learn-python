a = int(input("Enter Your Age: "))

if (a>=18):
    print("You can vote! ")
elif(a<0):
    print("Invalid Age")
elif(a == 0):
    print("You have entered age 0 which is not valid0")    
else:
    print("You can't vote")    