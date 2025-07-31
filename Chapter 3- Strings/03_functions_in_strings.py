#String Functions and Methods
name = 'Aamir'
print(name.upper())  # Converts the string to uppercase

str_2 = "Hello"
print(str_2.lower())  # Converts the string to lowercase

str_3 = "Aamir is learning Python"
print(str_3.title())  # Converts the first character of each word to uppercase
print(str_3.endswith("Python"))  # Checks if the string ends with "Python"
print(str_3.startswith("Aamir"))  # Checks if the string starts with "Aamir".
print(str_3.split())  # Splits the string into a list of words
print(str_3.split(" "))  # Splits the string using space as a delimiter
print(str_3.split("is"))  # Splits the string using "is" as a delimiter
print(str_3.replace("Aamir", "Ali"))  # Replaces "Aamir" with "Ali" in the string
print(str_3.find("learning"))  # Finds the index of the substring "learning"
print(str_3.index("Python"))  # Finds the index of the substring "Python"
print(str_3.count("Aamir"))  # Counts the occurrences of "Aamir" in the string
print(str_3.isalpha())  # Checks if the string contains only alphabetic characters
print(str_3.isalnum())  # Checks if the string contains only alphanumeric characters

# There are many more string functions and methods available in Python.
# You can explore them in the official Python documentation or by using the help() function..
#print(str_3.help())  # Displays help information for string methods