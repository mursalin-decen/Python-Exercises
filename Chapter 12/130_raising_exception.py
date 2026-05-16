a = int(input("Enter first number a : "))
b = int(input("Enter second number b : "))

if b==0 :
    raise ZeroDivisionError (f"Hey bruh you devide {a} by {b} my progrrame doesn't ment divde by zero ")
else:
    print (f"Ans is {a/b} ")