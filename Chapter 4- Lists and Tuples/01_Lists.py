#lists are container to store multiple items in a single variable
#lists are mutable, meaning they can be changed after creation
#lists are defined using square brackets []

random = ["Ali", 1, 3.14, True, 'A',]
#lists can contain different data types
print(random)
#lists can be accessed using indices, starting from 0
print(random[0])  # Output: Ali
print(random[1])  # Output: 1

#lists can be sliced to get a sublist
print(random[1:3])  # this means from index 1 to index 2 (3 is not included)
print(random[:3])  # this means from the start to index 2
print(random[2:])  # this means from index 2 to the end

#we talked about lists being mutable, we can change the value of an item in a list
random[0] = "Ahmed"
print(random)  # Output: ['Ahmed', 1, 3.14, True, 'A']