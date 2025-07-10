# Nested Dictionaries are dictionaries within dictionaries. They allow you to store complex data structures.
# Example of a nested dictionary
students = {
    "student1": {
        "name": "John",
        "age": 25,
        "courses": ["Math", "Science"]
    },
    "student2": {
        "name": "Jane",
        "age": 22,
        "courses": ["English", "History"]
    }
}
print(students)  # Printing the nested dictionary
# Accessing values in a nested dictionary
print(students["student1"]["name"])  # Accessing name of student1
print(students["student2"]["courses"])  # Accessing courses of student2
# Adding a new student to the nested dictionary
students["student3"] = {
    "name": "Alice",
    "age": 23,
    "courses": ["Biology", "Chemistry"]
}
# Updating a student's age in the nested dictionary
students["student1"]["age"] = 26
# Looping through the nested dictionary
for key, value in students.items():
    print(key, value["name"], value["age"], value["courses"])
# Deleting a student from the nested dictionary
# del students["student2"]