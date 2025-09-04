#This is how we write file

st = "Hey, you're amazing.You're doing good and going on a perfect path."

f = open("myfile.txt" , "w")  #"w" means the file is opened in write mode
f.write(st)
f.close()