#  Write a program to find out whether a given post is talking about “Python” or not.
post = "Python"
cmnt = input("Creat a Post: ")

if(post in cmnt):
    print(f"Given Post is talking about {post}")
else:
    print(f"Given Post is not talking about {post}")