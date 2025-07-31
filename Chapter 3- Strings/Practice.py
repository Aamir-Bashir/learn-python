# Write a Python program to display user entered name followed by a greeting message.
name = input("ENTER YOUR NAME: ")
print(f"Good Afternoon {name}! Welcome to Python Programming")

# Write a program to fill in letter template with name and date.
letter = ''' 
    Dear ,<|Name|>
    You are selected!
    Date: <|Date|>
'''
print(letter.replace("<|Name|>", name).replace("<|Date|>", "01/01/2023"))

# Write a Program to detect double spaces in a string.
name = "Aamir  Bashir  Khan"
print(name.find("  "))  # Returns the index of the first occurrence of double space
# Write a program to replace double spaces with single space in a string.
name = name.replace("  ", " ")
print(name)  # Output: "Aamir Bashir Khan"

# Write a program to format a string using escape sequences.
format_string = "Aamir is a good learner He is learning Python"
formatted_string = "Aamir is a good learner \nHe is learning Python"  # Using newline escape sequence
print(formatted_string)

