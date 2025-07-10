# Dictionaries are used to store data values in key:value pairs.
students = {
    "name": "John",   
    "age": 25,
   "courses": ["Math", "Science"],} # this is a dictionary with three key-value pairs

#Methods to access values in a dictionary
print(students["name"])  # Accessing value using key
print(students.get("age"))  # Accessing value using get method
print(students.get("phone", "Not Found"))  # Accessing a non-existing key with a default value
# Adding a new key-value pair
students["phone"] = "123-456-7890"
print(students)
# Updating an existing key-value pair
students.update({"age": 26, "city": "New York"})
print(students)

#loops through a dictionary
for key, value in students.items():
    print(key ,value)