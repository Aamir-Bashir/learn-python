#Basic way to create a class and a object too 
#We will also understand instance attributes and class attributes here too

class Employee:
    language = "Python" # this is a class attribute
    salary = 2000000

Aamir = Employee()
Aamir.name = "Aamir" #This is a instance(Object) attribute
print(Aamir.name , Aamir.language, Aamir.salary)

Ali = Employee()
Ali.name = "Ali" #This is a instance(Object) attribute
print(Ali.name , Aamir.language, Aamir.salary)

#Here name is an instance attribute and language and salary aare class attribute as they directly belong to the class