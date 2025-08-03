#Dictionaries are mutable, unordered collections of items.
#They are defined using curly braces {} and consist of key-value pairs.
#empty dictionary

D = {} #this is an empty dictionary
print(type(D)) 

dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"}
print(dict)
#Accessing values in a dictionary using keys
print(dict["name"])  # Output: Alice
