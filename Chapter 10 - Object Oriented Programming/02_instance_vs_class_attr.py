class Employee:
    language = "Python" # this is a class attribute
    salary = 2000000

Aamir = Employee()
Aamir.language = "Java" #This is a instance(Object) attribute
print(Aamir.language, Aamir.salary)
#Above program will print Java instead of Python Because Instance attributes,take preference over class attributes during assignment and rretrieval.

