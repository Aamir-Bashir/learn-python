'''
Suppose there is a very long string with emails and we wrote a program to extract emails
eg:
   a = "a very long string with emails"

   emails = []
The program took 3 seconds to run
Now will that emails will be stored anywhere? NO.
To store the generated data we use file
'''

f = open("file.txt")
data = f.read()
print(data)
f.close

'''
There are different modes of opening file

r - opening for reading ------ this is default
w - open for writing
a - open for appending
+ - open for updating
rb - read in binary 
rt - will open for read in text mode.
'''