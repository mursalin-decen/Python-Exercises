'''
4. A file contains a word “Donkey” multiple times. You need to write a program
which replace this word with ##### by updating the same file.
5. Repeat program 4 for a list of such words to be censored.
'''

l1= ["donkey", "gandu", "fuck", "sex"]

with open("donkey.txt", "r") as f:
    content = f.read()

for word in l1:
    content =content.replace(word,"#"*len(word))
with open("donkey.txt", "w") as f:
    f.write(content)
