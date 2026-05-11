class Employee:
    company = "ICT"
    name = "Zamzam"
    def show(self):
        print(f"The name of employee{self.name} and their company {self.company}")

class Coder:
    language = 'Python'
    def printlanguage(self):
        print(f"Here is some language but you prefer : {self.language} ")

# class Programmer():
#     company = "Google"
#     def show(self):
#         print(f"The name of employee{self.name} and their company {self.salary}")
class Programmer(Employee,Coder):
    company = "Janina"
    def showLanguage(self):
        print(f"His lamgugae is {self.language}, {self.name} is good on this")



a=Employee()
b=Programmer()

b.show()
b.printlanguage()
b.showLanguage()