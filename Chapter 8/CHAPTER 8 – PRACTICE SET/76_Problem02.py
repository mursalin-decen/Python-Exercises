# 2. Write a python program using function to convert Celsius to Fahrenheit.
def convert(C):
    F = (C * 1.8) + 32
    return F
C=int(input("Enter num: "))

rslt =convert(C)
print(rslt)