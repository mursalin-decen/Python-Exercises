# 5. Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *


def pattarn(n):
    for i in range(n,0,-1):
       
        print("*"*i, end=" ")
        print("")

n= int(input("Enter number: "))

pattarn(n)

