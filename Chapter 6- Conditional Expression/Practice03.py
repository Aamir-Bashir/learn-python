#Write a program to detect spam comments.

c1 = "Make alot of money"
c2 = "click this"
c3 = "buy now"
c4 = "subscribe this"

message = input("Enter Your Comment: ")

if((c1 in message) or (c2 in message) or (c3 in message) or (c4 in message) ):
    print("This Comment is a spam")
else:
    print("This Comment is not a spam")    