#1. Write a program to find the greatest of four numbers entered by the user.
num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))
num3 = int(input("enter a number: "))
num4 = int(input("enter a number: "))

if(num1>num2 and num1>num3 and num1>num4):
    print(f"{num1} is greatest")

elif(num2>num1 and num2>num3 and num1>num4):
    print(f"{num2} is greatest")
    
elif(num3>num2 and num3>num1 and num3>num4):
    print(f"{num3} is greatest")

elif(num4>num2 and num4>num3 and num4>num1):
    print(f"{num4} is greatest")
