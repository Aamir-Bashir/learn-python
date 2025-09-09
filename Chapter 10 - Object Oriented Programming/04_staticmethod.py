# To avoid self in a function where there is no need we use @static method

class Employee:
    language = "Python" # this is a class attribute
    salary = 2000000

    def getinfo(self):
        print(f"The Language is {self.language} and the salary is {self.salary}")
    
    @staticmethod
    def greet(): #here in greet function we don't need any  self so we will use static here
        print("Good Morning")

Aamir = Employee()
Aamir.language = "Java" #This is a instance(Object) attribute
print(Aamir.language, Aamir.salary)
Aamir.greet()
Aamir.getinfo()

#It's not necessary to write "self" you can give any name but mostly self is used