# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
#from problem _6
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
#If the names of 2 friends are same, the latest value will overwrite the 
# previous value because duplicate keys are not allowed in a dictionary.