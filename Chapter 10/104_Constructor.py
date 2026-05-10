#__init_
class Employee:
    
    language = "Bangla" #This is a class atribute
    salary = 100000
    def getinfo(self): #must be give a parameter self if you dont then give error
      print(f"The language is{self.language}.The salary is{self.salary}")
    
    def __init__(self,name, salary, language):
       self.name = name
       self.salary = salary
       self.language = language
       print("I am creating an object")
    def __str__(self):
        return f"{self.name} {self.salary} {self.language}"
       

    

zam = Employee("ZAzam",12000,"Nepali")
print(zam)