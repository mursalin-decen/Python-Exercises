# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

mark = int(input("Enter mark : "))

if((mark>100) or (mark<0)):
    print("invalid")

elif(mark>=90):
    print("Ex")
elif(mark>=80):
    print('A')
elif(mark>=70):
    print('B')
elif(mark>=60):
    print("C")
elif(mark>=50):
    print('D')
else:
    print('F')

