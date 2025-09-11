#Create a class "Programmer" for storing information of few programmers

class Programmer:
    company = "Microsoft"

    def __init__(self , name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin

a = Programmer("Aamir" , 1200000 , 3452)
print(a.name , a.company , a.salary , a.pin)
b = Programmer("Ali" , 1200000 , 3453)
print(b.name , b.company , b.salary , b.pin)
        