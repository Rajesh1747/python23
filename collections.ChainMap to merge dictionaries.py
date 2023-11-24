from collections import ChainMap
# Creating dictionaries
dict1 = {'name': 'Rajesh'}
dict2 = {'age': 30, 'city': 'New York'}

# Merging dictionaries using ChainMap
merged_dict = ChainMap(dict1, dict2)

# Displaying the merged dictionary
print(dict(merged_dict))