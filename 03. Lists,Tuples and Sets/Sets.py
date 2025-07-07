# Sets are unordered and contains no duplicate elements.
cs_courses = {'Python', 'Java', 'C++', 'JavaScript', 'Ruby', 'Python'}  #this is a set of courses
print(cs_courses)  
#Now this will print the set of courses without any particular order and without any duplicate elements.

Science_courses = {'Physics', 'Chemistry', 'Biology', 'Mathematics', 'History'}
Art_courses = {'Painting', 'Sculpture', 'Photography', 'History', 'Mathematics'}
# Sets can be used to perform mathematical operations like union, intersection, difference, and symmetric difference.
# Union: Combines all unique elements from both sets
all_courses = Art_courses.union(Science_courses )  #this will combine all unique elements from both Art_courses and Science_courses
print(all_courses)
# Intersection: Finds common elements between sets
common_courses = Science_courses.intersection(Art_courses)  #this wil find elements that are common in both Science_courses and Art_courses
print(common_courses) 
# Difference: Finds elements in one set that are not in another
unique_cs_courses = Art_courses.difference(Science_courses)  #this will find elements that are in Art_courses but not in Science_courses
print(unique_cs_courses)
# Symmetric Difference: Finds elements that are in either set but not in both
symmetric_difference_courses = Science_courses.symmetric_difference(Art_courses)  #this will find elements that are in either Science_courses or Art_courses but not in both
print(symmetric_difference_courses)

# Empty collections in Python

# Empty list
empty_list = []  #this is an empty list
empty_list = list() #this is also an empty list

# Empty tuple
empty_tuple = ()  #this is an empty tuple
empty_tuple = tuple()  #this is also an empty tuple

# Empty set
empty_set = {} #this is not an empty set, this is a dictionary
# To create an empty set, we need to use the set() constructor
empty_set = set()  #this is an empty set
