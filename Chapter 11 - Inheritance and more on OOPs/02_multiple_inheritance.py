
class Employee():
    name = "Default Name"
    company = "Microsoft"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Pyhton"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")


class Programmer(Employee , Coder):
    company = "Apple"
    def showlanguage(self):
        print(f"The company name is {self.company} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showlanguage()    