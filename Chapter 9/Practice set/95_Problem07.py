'''
6. Write a program to mine a log file and find out whether it contains ‘python’.
7. Write a program to find out the line number where python is present from ques 6.
'''

with open("log.txt","r") as f:
   lines = f.readlines()
lineno=1
for line in lines :
    if("python" in line):
        print(f"Found Python in line {lineno}")
        break
    lineno+=1
else:
    print("No python found")