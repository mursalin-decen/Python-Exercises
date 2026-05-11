class number:
    def __init__(self,n):
        self.n = n
    
    def __add__(self, num):
         return self.n + num.n
    
    def __sub__(self, num):
        return self.n -num.n
        


n = number(3)
m = number(8)

print(n+m)
print(n-m)
        