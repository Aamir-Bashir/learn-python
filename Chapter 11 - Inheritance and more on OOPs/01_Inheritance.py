#Inheritance is a way of creating class from an existing class

class Employee():
    company = "Microsoft"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

# class Programmer:
#     company = "Apple"
#     def show(self):
#         print(f"The name of the employee is {self.name} and the salary is {self.salary}")

#     def showlanguage(self):
#         print(f"The name of the employee is {self.name} and he is good with {self.language} language")

"""
We can write the pogram the above way to but this is very much error prone and not a sufficient way so 
for that we use inheritance we derive a class from the base class 
"""



class Programmer(Employee):
    company = "Apple"
    def showlanguage(self):
        print(f"The name of the employee is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer

print(a.company , b.company)
    