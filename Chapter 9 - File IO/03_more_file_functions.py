f = open("file.txt")
# lines = f.readlines() #readlines returns a the list of our lines in our file
# print(lines , type(lines))
# f.close()

#readline returns each line 

#For example
# line1 = f.readline()
# print(line1 , type(line1))

# line2 = f.readline()
# print(line2 , type(line2))

# line3 = f.readline()
# print(line3 , type(line3))

# line4 = f.readline()
# print(line4 , type(line4))

#This same thing can be done in a loop
#for example

line = f.readline
while(line != ""):
    print(line)
    line = f.readline()

f.close() 