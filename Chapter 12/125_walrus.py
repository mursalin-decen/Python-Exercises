#using walrus operator
if (n:=len([1,2,3,56,3,4,5]))>3:
    print(f"List is too long ({n} elemnts, expected <=3)")