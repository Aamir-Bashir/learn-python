random = ["Ali", 1, 3.14, True, 'A',]
print(random)  # Output: ['Ali', 1, 3.14, True, 'A']

random.append("New Item")  # Adding a new item to the end of the list
print(random)  # Output: ['Ali', 1, 3.14, True, 'A', 'New Item']

l1 = [1, 5, 3, 2, 45, 32, 12]
l1.sort()  # Sorting the list in ascending order
print(l1)  # Output: [1, 2, 3, 5, 12, 32, 45]

l2 = [1, 2, 3, 4, 5]
l2.reverse()  # Reversing the order of the list
print(l2)  # Output: [5, 4, 3, 2, 1]

l3 = [1, 4, 2, 3]
l3.remove(4)  # Removing the first occurrence of the value 4 from the list
print(l3)  # Output: [1, 2, 3]

l4 = [1, 2, 3, 4, 5]
l4.insert(2, 10)  # Inserting the value 10 at index 2
print(l4)  # Output: [1, 2, 10, 3, 4, 5]

l5 = [1, 2, 3, 4, 5]
l5.pop(2)  # Removing the item at index 2  
print(l5)  # Output: [1, 2, 3, 4]

#These are some common list methods , there are many more methods available in Python to manipulate lists.
# for example 
l6 = [1, 2, 3, 4, 5]
print(l6.count(3))  # Counting the occurrences of the value 3 in the list  # Output: 1
# like these methods, you can explore more methods in the Python documentation.
