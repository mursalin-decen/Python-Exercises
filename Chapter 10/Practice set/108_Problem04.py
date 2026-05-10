# 4. Add a static method in problem 2, to greet the user with hello.
# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.
import math
class Calculator:
    @staticmethod
    def greet():
        print("Hello")

    def __init__(self,n):
        self.n = n
    def squre(self):
        print(f"The squre is: {self.n*self.n}")
    def squreroot(self):
        print(f"The squreroot is: {math.sqrt(self.n)}")
    def cube(self):
        print(f"The squre is: {self.n*self.n*self.n}")

n = int(input("Enter your number: "))

a = Calculator(n)
a.greet()
a.squre()
a.squreroot()
a.cube()