# Creating an empty dictionary
person={}
print(person)

# Adding a single key-value pair
person['name']='Rajesh'
print(person)

#Adding multiple key-value pairs using update()
person=({ 'age':'23', 'state':'Anantapur'})
print(person)

#Adding key-value pairs using dictionary
new_font={'age':'23','state':'Anantapur'}
person={**person,**new_font}
print(person)

#using setdefault() to add a new key value pair
person.setdefault('age',30)
print(person)