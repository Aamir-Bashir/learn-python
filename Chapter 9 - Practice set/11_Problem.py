#Rename a file
#Simply to rename a file write the content in another file and delete the existing file
#for example

with open("old.txt") as f:
    content = f.read()

with open("rename.txt" , "w") as f:
    f.write(content)