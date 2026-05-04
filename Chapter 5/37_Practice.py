#8. If languages of two friends are same; what will happen to the program in problem 6?
dir={}

name = input("Enter friend name: ")
lang = input("Enter his/her language: ")
dir.update({name:lang})
name = input("Enter friend name: ")
lang = input("Enter his/her language: ")
dir.update({name:lang})
name = input("Enter friend name: ")
lang = input("Enter his/her language: ")
dir.update({name:lang})
name = input("Enter friend name: ")
lang = input("Enter his/her language: ")
dir.update({name:lang})
print(dir)
#Nothing will happend cause value can be same