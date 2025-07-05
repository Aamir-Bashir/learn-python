single_qoute = 'This is a single quote string'
double_quote = "This is a double quote string"
triple_quote = """This is a triple single quote string
Which can print multiple lines
and is useful for long text."""
print(single_qoute)
print(double_quote)
print(triple_quote)

#SLICING STRINGS
print(double_quote[3])   #this will print the 4th character of the string because indexing starts at 0
print(double_quote[3:10])  #this will print the characters from index 3 to index 10
print(double_quote[3:])  #this will print the characters from index 3 to    the end of the string
print(double_quote[:10])  #this will print the characters from the start of the string to index 10
print(double_quote[-1])  #this will print the last character of the string 
print(double_quote[-3:])  #this will print the last 3 characters of the string
