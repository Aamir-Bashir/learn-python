f = open("file.txt")
print(f.read())
f.close

# the  same way can be written like this
with open("file.txt" ) as f:
    print(f.read())

#You don't have to explicity close the file                                                                                                                                                                                                