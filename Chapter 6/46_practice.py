# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

spam= ["Make a lot of money","buy now","subscribe this", "click this"]
comment =input("Enter Comment here: ")

if((spam[0] in comment)or 
(spam[1] in comment)or     #use -----in----- key word 
(spam[2] in comment)or 
(spam[3] in comment) ):
    print("Scam Detected")

else:
    print("Everything is ok")

# a="Make a lot of money"
# b="buy now"
# c="subscribe this"
# d= "click this"

# cmnt = input("Enter comment: ")

# if((a in cmnt ) or (b in cmnt) or (c in cmnt) or (d in cmnt)):
#     print("Spammer")

# else:
#     print("Ok now")