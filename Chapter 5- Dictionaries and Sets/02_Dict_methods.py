marks = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78,
    2: "Ali" # We can also use integers as keys
}
print(marks)

# print(marks.items())  # Output: dict_items([('Alice', 85), ('Bob', 90), ('Charlie', 78)])
# print(marks.keys())  # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
# print(marks.values())  # Output: dict_values([85, 90, 78])

marks.update({"David": 88 , "Aamir": 100})  # Adding a new key-value pair
print(marks)

print(marks.get("Alice"))  # returns none if the key does not exist
print(marks["Bob"]) #returns error if the key does not exist  #you can change the name and check the output
#more methods can be found in the documentation in Python's official site