# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.
# 5. Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x +other.x , self.y + other.y , self.z +other.z)
        return result
    
    def __mul__(self, other):
        result1 = (self.x *other.x +self.y *other.y + self.z*other.z)
        return result1
    def __str__(self):
        return f"Vector {self.x}, {self.y} , {self.z} "
    
    def __len__(self):
        return 3

v1 = Vector(1,2,3)
v2 = Vector(3,3,4)
v3 = Vector(4,1,3)

print(v1+v2)
print(v2*v3)
print(len(v1))
        