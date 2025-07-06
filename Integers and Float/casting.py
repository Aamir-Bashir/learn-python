#sometimes we can run into issue of typing integers as strings and then we need to convert them to integers
num1 = "10"
num2 = "20"
# num1 = "10" num2 = "20" if we try to add them without converting, it will concatenate the strings

# num1 = "10" + num2 = "20" will result in "1020" as a string
# to avoid this, we convert them to integers first


# converting strings to integers
num1 = int(num1)
num2 = int(num2)
print(num1 + num2)  # this will now work as both are integers