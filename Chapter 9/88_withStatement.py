
# f= open("file.txt","r") # "r" for read file
# data = f.read()
# print(data)
# f.close()
# Open the file in read mode using 'with', which automatically closes thefile
with open("file.txt", "r") as f:
# Read the contents of the file
    text = f.read()
# Print the contents
print(text)