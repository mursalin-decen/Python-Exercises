# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class Programmer:
    WorkPlace  = "Microsoft"
    Category = "Programmer"

    def __init__(self,name):
        self.name = name
      
    def __str__(self):
            return f"Name: {self.name},WorkPlace: {self.WorkPlace}, Category: {self.Category}"


m1 = Programmer ("Zam")
m2 = Programmer ("Shi")
print(m1)
print(m2)