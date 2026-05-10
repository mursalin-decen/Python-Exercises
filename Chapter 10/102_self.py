class Employee:
    
    language = "Bangla" #This is a class atribute
    salary = 100000
    def getinfo(self): #must be give a parameter self if you dont then give error
      print(f"The language is{self.language}.The salary is{self.salary}")
    

zam= Employee()
zam.language ="Python"
zam.name= "Zamzam" #this is an instance attribute
print( zam.language, zam.salary)

zam.getinfo() #as same as Employee.getinfo(self)