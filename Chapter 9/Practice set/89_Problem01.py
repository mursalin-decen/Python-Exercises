# 1.Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.
f = open("poems.txt", "r")
data = f.read()

b= "Twinkle"

if b in  data:
    print("Find word")

else: 
    print("Not found")

f.close()