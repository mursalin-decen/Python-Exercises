# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

num=int(input("Enter number: "))
for i in range(1,num+1):
    print(" "*(num-i), end=" ") # end=" " if we write this then don't break the line
    print("*"*(2*i-1), end="") #odd number = (2*i-1)= (2*1-1)=(2*2-1)
    print("")