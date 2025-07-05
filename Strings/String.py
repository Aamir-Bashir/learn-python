single_qoute = 'This is a single quote string'
double_quote = "This is a double quote string"
triple_quote = """This is a triple single quote string
Which can print multiple lines
and is useful for long text."""
print(single_qoute)
print(double_quote)
print(triple_quote)


greeting = "Hello"
name = "Mohamed"
print(dir(greeting))     #this will print all the attributes and methods of the string object that we have access to that variable now
# STRING OPERATIONS and METHODS
print(single_qoute + " " + double_quote)  #this will concatenate the two strings
message = '{}, {}. Welcome! '.format(greeting , name)  #this will concat the two strings using format method this is useful for longer and complicated strings
print(f"{greeting}, {name.upper()}. Welcome!")  #this is a f-string, a more modern way to format strings
print(message)  #this will print the formatted message
print(single_qoute * 2)  #this will repeat the string twice
print(type(double_quote))  #this will print the type of the variable
print(double_quote.upper())  #this will convert the string to uppercase
print(double_quote.lower())  #this will convert the string to lowercase
print(double_quote.title())  #this will convert the string to title case
print(double_quote.replace("double", "triple"))  #this will replace the word 'double' with 'triple'
print(double_quote.find("double"))  #this will find the index of the word 'double' in the string
print(double_quote.count("is"))  #this will count the number of occurrences of the word 'is' in the string
print(double_quote.split(" "))  #this will split the string into a list of words
print(double_quote.split("is"))  #this will split the string into a list of words using 'is' as the delimiter
print(double_quote.strip())  #this will remove any leading or trailing whitespace from the string
print(double_quote.startswith("This"))  #this will check if the string starts with 'This'
print(double_quote.endswith("string"))  #this will check if the string ends with 'string'
print(len(double_quote))   #this will print the length of the string

#SLICING STRINGS
print(double_quote[3])   #this will print the 4th character of the string because indexing starts at 0
print(double_quote[3:10])  #this will print the characters from index 3 to index 10
print(double_quote[3:])  #this will print the characters from index 3 to    the end of the string
print(double_quote[:10])  #this will print the characters from the start of the string to index 10
print(double_quote[-1])  #this will print the last character of the string 
print(double_quote[-3:])  #this will print the last 3 characters of the string

print(help(str))  #this will print the information about the string class and its methods