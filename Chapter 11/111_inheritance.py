class Employee:
    company = "ICT"
    def show(self):
        
        print(f"The name of employee{self.name} and their company {self.salary}")

# class Programmer():
#     company = "Google"
#     def show(self):
#         print(f"The name of employee{self.name} and their company {self.salary}")
class Programmer(Employee):
    company = "Janina"
    def showLanguage(self):
        print(f"His lamgugae is {self.language}, {self.name} is good on this")


a = Employee()
b=Programmer()

print(a.company, b.company)