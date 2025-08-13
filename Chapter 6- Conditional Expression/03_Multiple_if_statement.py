a = int(input("Enter Your Age: "))
# If statement No. 1
if (a%2 == 0):
    print("Even ")
else: 
    print("Odd ")    
 #End of if statement No. 1

 # if statement No.2   
if (a>=18):
    print("You can vote! ")
elif(a<0):
    print("Invalid Age")
elif(a == 0):
    print("You have entered age 0 which is not valid0")    
else:
    print("You can't vote")

 #End of if statement No. 2       

 #There can be multiple ifs more than even two but every if will be independent.