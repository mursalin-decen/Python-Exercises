'''2. Write a program to greet all the person names stored in a list ‘l’ and which starts
with S.
l = ["Zam", "Soham", "Shi", "Shoma"]'''

l = ["Zam", "Soham", "Shi", "Shoma"]
for i in l:
    if(i.startswith("S")):
        print(f"Hello {i}")
