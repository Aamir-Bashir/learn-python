string = "Aamir"
#slicing
# Slicing allows you to extract a portion of a string
# Syntax: string[start:end]
#indexing starts from 0
sliced_string = string[1:4]  # Extracts characters from index 1 to 3 (exclusive of index 4)
print(sliced_string)  # Output: "ami"
sliced_string2 = string[:5] # Extracts characters from the 0th index to the 4th index (exclusive of index 5)
print(sliced_string2)  # Output: "Aamir"
sliced_string3 = string[2:]  # Extracts characters from index 2 to the end of the string
print(sliced_string3)  # Output: "amir"

# Negative Slicing
negative_sliced_string = string[-4:-1]  # Extracts characters from index -4 to -2 (exclusive of -1)
print(negative_sliced_string)  # Output: "ami"

# Slicing with Skip value
sliced_string_with_skip = string[0:5:2]  # Extracts characters from index 0 to 4 with a step of 2
print(sliced_string_with_skip)  # Output: "Amr"  