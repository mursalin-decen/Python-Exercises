#ধর তোমারে বলছে যে ভাই তোমারে একটা কাজ করা লাগবে যদি কেও ১৮ বছরের নিছে এই ওয়েব সাইটে ঢুকে অরে বলবা
#ভাই তুমি ১৮ এর নিচে আর যারা বড় তাদের বলবা ওয়েলকাম।

#it is, if elif else ladder
age = int(input("Enter your age: "))

#if condition no1 start :
if(age%2== 0):
    print("its a even number") #here this if is alone it will give output only its base.
                               #with this if no connection with others remember this.

#if condition no1 end :

#if condition no2 start :
if(age>= 18):
    print("\"WELCOME\"")

elif(age<0):
    print("You entered an invalid age")

elif(age == 0):
    print("Your entered age is 0 its not valid")

else:
    print("Sorry, You are under 18")
#if condition no2 end :
print("Captcha Verification END")