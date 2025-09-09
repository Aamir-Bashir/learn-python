class Employee:
    language = "Python" 
    salary = 2000000
    def __init__(self , name , language , salary): #dunder method , it is called automatically
        self.name = name
        self.language = language
        self.salary = salary
        
    def getinfo(self):
        print(f"The Language is {self.language} and the salary is {self.salary}")
    
    @staticmethod
    def greet(): 
        print("Good Morning")

Aamir = Employee("Aamir" , "Python" , 1200000)
print(Aamir.name , Aamir.language , Aamir.salary)

