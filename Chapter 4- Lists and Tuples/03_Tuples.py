#Tuples are immutable sequences in Python, similar to lists but with fixed size and content.
#Tuples are defined using parentheses ()
random = ("Ali", 1, 3.14, True, 'A',)
#Tuples can contain different data types
print(random)  # Output: ('Ali', 1, 3.14, True, 'A')

#empty tuple
empty_tuple = ()
#Tuple that has single item must have a comma
single_item_tuple = (1,)  # Note the comma , if you don't add a comma, it will be treated as an integer
print(empty_tuple)  # Output: ()
print(single_item_tuple)  # Output: (1,)

