#here we will do the same main.py code but with different and shortened way

'''
We will create a snake , water and gun game
in which computer will choose random numbers from -1, 0 , 1
-1 = Water
0 = Gun
1 = Snake
'''
import random

computer = random.choice([-1, 0 , 1])
youstr = input("Enter Your Choice: ")
youDict = {"s": 1 , "w":-1 , "g":0}
reverseDict = {1: "Snake" , -1: "Water" , 0: "Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")

else: 
     '''if(computer == -1 and you == 1): (computer - you) = -2
         print("You Win!")

     elif(computer == -1 and you == 0): (computer - you) = -1
         print("You Lose!")

     elif(computer == 1 and you == -1): (computer - you) = 2
         print("You Lose!")

     elif(computer == 1 and you == 0): (computer - you) = 1
         print("You Win!")        

     elif(computer == 0 and you == -1): (computer - you) = 1
         print("You Win!")

     elif(computer == 0 and you == 1): (computer - you) = -1
         print("You Lose!")

     else: 
         print("Something went wrong!") 
         
         The Below logic is written on the basis of the value of computer - you
         '''
if((computer - you) == -1 or (computer - you) == 2):
    print("You Lose!")
else:
    print("You Win!")   