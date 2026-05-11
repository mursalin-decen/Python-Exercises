class Employee:
    a=2


class Programmer(Employee):
    b=3


class Coder(Programmer):
    c=4



ob1 = Employee()
print(ob1.a)
# print(ob1.b) making error
ob2 = Coder()
print(ob2.a, ob2.b, ob2.c)
