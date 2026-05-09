# 9. Write a program to find out whether a file is identical & matches the content of
# another file.
with open ("this.txt", "r") as f:
  data1 =  f.read()

with open("this_copy.txt", "r") as f:
   data2 = f.read()


if(data1 == data2):
   print("This file is identical & matches")
else:
    print("No match found")