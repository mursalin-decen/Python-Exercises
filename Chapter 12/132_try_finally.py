# try:
#     a = int(input("Enter a number : " ))
#     print(a)

# except ValueError as v:
#     print(v)
    
# except Exception as e:
#     print(e)

# finally:
#     print("Thank You") # you can see there if thje block is wrong then it will aslo fiving last block

#then where is the use of finally???? 
# let me show you, actually finally use on function


def show():
    try:
     a = int(input("Enter a number : " ))
     print(a)
     return
    except ValueError as v:
        print(v)
        return
    except Exception as e:
         print(e)
         return
    finally:
      print("Thank You")


show()