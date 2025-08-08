#What will be the length of  following set

s = set()
s.add(20)
s.add('20')
s.add(20.0)

print(s , len(s))


#We thought that the length will be 3 but python compares the value of floating-point nuumbers and int if they are numerically equal it gives true no matter what  the datatype is for that reason this sets value will be true
