class Employee:
    language = "Python" # this is a class attribute
    salary = 2000000

    def getinfo(self): #If we don't give self parameter in the function here it would have given error saying "TypeError: Employee.getifo() takes 0 positional argument but one was given so, to accept the argument we give self argument."
        print(f"The Language is {self.language} and the salary is {self.salary}")
    
    def greet(self): #Even if we use self or not but we need no give it because without ir there will be error
        print("Good Morning")

Aamir = Employee()
Aamir.language = "Java" #This is a instance(Object) attribute
print(Aamir.language, Aamir.salary)
Aamir.greet()
Aamir.getinfo()
# Employee.greet(Aamir)
# Employee.getinfo(Aamir)

#It's not necessary to write "self" you can give any name but mostly self is used