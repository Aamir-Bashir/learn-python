random = ("Ali", 1, 3.14, True, 'A',)
print(random)  # Output: ('Ali', 1, 3.14, True, 'A')
print(len(random))  # Output: 5, getting the length of the tuple

#methods for tuples
# Tuples do not have methods like lists, but we can use some built-in functions

no = random.count('A')  # Counting the occurrences of 'A' in the tuple
print(no)  # Output: 1

no2 = random.index(3.14)  # Finding the index of the value 3.14 in the tuple
print(no2)  # Output: 2

# Tuples can be concatenated using the + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2  # Concatenating two tuples
print(concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6)

