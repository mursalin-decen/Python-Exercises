#Suppose you need to write a code for  avarage mark many times.so what shoud you do??
#Would you write that code agin ang again. LOl lets make it easy
print("Without funtion:")
mark1 = int(input("Enter mark for Bangla: "))
mark2 = int(input("Enter mark for English: "))
mark3 = int(input("Enter mark for Math: "))

avarage = (mark1+mark2+mark3)/3

print(f"Your avarage mark is {avarage}")
print(" ")
#now if we need to make this 100 times then what should you do bruhh.. for this we can use a functions , Lets see:

def avg(): #its name is funtion definetion remember
    mark1 = int(input("Enter mark for Bangla: "))
    mark2 = int(input("Enter mark for English: "))
    mark3 = int(input("Enter mark for Math: "))

    avarage = (mark1+mark2+mark3)/3

    print(f"Your avarage mark is {avarage}")

avg() #its name is function call
avg()
avg()
