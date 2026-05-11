class Employee:
    def __init__(self):
        print("Employee class Constructor")
    a=2
class Programmer(Employee):
    def __init__(self):
         print("Programmer class Constructor")

    b=3


class Coder(Programmer):
    def __init__(self):
         super().__init__()
         print("Coder class Constructor")
    c=4



ob1 = Employee()
print(ob1.a)
# print(ob1.b) making error
ob2 = Coder()
print(ob2.a, ob2.b, ob2.c)
