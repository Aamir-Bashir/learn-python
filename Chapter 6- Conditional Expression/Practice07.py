# Write a program to find whether the post talks about Aamir or not

post = input("Enter Your post: ")

if("Aamir".lower() in post.lower()): #We can also writes if("aamir" in post.lower()) we write this method because no matter how the user writes it will detect te name 
    print("This Post Talks About Aamir")
else: 
    print("This Post Doesn't Talk About Aamir")
