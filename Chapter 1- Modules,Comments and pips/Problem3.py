#Write any program and label it with comments
#We will take a program which prints contents of a directory using os module
#We will use chatgpt to generate the code

import os

# Select the directory path you want to list
directory_path = '/projects' 

#Use the os module to list the contents of the directory
contents = os.listdir(directory_path)

# Print the contents of the directory
print(contents)