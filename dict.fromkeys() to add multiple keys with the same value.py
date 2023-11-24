# Creating a dictionary with multiple keys having the same value
keys = ['name', 'age', 'city']
default_value = 'unknow'
my_dict = dict.fromkeys(keys, default_value)

# Displaying the created dictionary
print(my_dict)