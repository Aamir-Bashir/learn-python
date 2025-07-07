#Differencs between Tuples and Lists
# 1. Tuples are immutable, meaning they cannot be changed after creation, while lists are mutable and can be modified.
# 2. Tuples are defined using parentheses (), while lists are defined using square brackets []

#Mutable
list_1 = ['maths', 'physics', 'chemistry', 'biology', 'computer science']  
list_2 = list_1
list_1[0] = 'english'  # this will change the first item in list_1 to 'english'
print(list_1)  # Output: ['english', 'physics', 'chemistry', 'biology', 'computer science']
print(list_2)  # Output: ['english', 'physics', 'chemistry', 'biology', 'computer science']


#Immutable
tuple_1 = ('maths', 'physics', 'chemistry', 'biology', 'computer science')
tuple_2 = tuple_1
# tuple_1[0] = 'english'  # This will raise a TypeError because tuples are immutable.
print(tuple_1)  # Output: ('maths', 'physics', 'chemistry', 'biology', 'computer science')
print(tuple_2)  # Output: ('maths', 'physics', 'chemistry', 'biology', 'computer science')

# Tuples can not be modified that's why there are no methods like append, remove, extend, insert, pop, sort, reverse in tuples.
# However, They behave pretty much same as lists , we can loop through them, access items by index, and use slicing.