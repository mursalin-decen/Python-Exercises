# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.
class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    
    def __add__(self, C):
        return Complex(self.r+C.r , self.i +C.i)
    
    def __mul__(self, C):
        real_part = self.r *C.r - self.i* C.i
        img_part = self.r *C.i + self.i *C.r

        return Complex(real_part, img_part)
        

    def __str__(self):
        return f" {self.r} + {self.i}i"
    
    


a=Complex(2, 3)
b=Complex(4, 4)

print(a+b)
print(a*b)

        