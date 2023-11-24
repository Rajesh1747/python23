# Creating an existing dictionary
person = {'name': 'Sandy'}

# Adding key-value pairs using dictionary comprehension
new_pairs = {'age': 23, 'city': 'New York'}
person= {**person, **new_pairs}

# Displaying the updated dictionary
print(person)