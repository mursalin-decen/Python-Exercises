# 4. Write a program to find whether a given username contains less than 10
# characters or not.

username = input('Enter your username less than 10 : ')

if(len(username)<10):
    print("Username contains less than 10 characters")

else:
    print("Username is 10 or more characters")
