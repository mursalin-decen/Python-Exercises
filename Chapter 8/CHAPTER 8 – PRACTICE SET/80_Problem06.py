
# 6. Write a python function which converts inches to cms.

def convert(n):
    Cms = n*2.54
    return Cms
n= float(input('Enter number: '))

rslt = convert(n)
print(rslt)