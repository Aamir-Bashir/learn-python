# create an empty dictionary . Allow 4 friends to enter their favorite language as value and use key as their names.Assume that the names are unique.

dict = {}
name = input("Enter Friends Name: ")
lang = input("Enter Friends Language: ")
dict.update({name : lang})

name = input("Enter Friends Name: ")
lang = input("Enter Friends Language: ")
dict.update({name : lang})

name = input("Enter Friends Name: ")
lang = input("Enter Friends Language: ")
dict.update({name : lang})

name = input("Enter Friends Name: ")
lang = input("Enter Friends Language: ")
dict.update({name : lang})

print(dict)

#If we input the same name it will update according to the language you select
# for example if you input Ali and Python and then again Ali and C++ it will update the value of Ali to C++
#if you input same value for two friends like same language so, values can be same it will only update the key