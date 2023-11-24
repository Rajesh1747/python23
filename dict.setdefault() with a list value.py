# Creating an empty dictionary
my_dict = {}

# Using setdefault() with a list value to add multiple values to a key
my_dict.setdefault('numbers', []).extend([9, 2, 3])

# Displaying the updated dictionary
print(my_dict)