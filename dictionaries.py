# Unordered, changeable, indexed - no duplicates

# Create dict
person = {
    'first': 'Jake',
    'last': 'Ike',
    'age': 23
}
print(person, type(person))

# Use constructor
person2 = dict(firstname="Sara", lastname="Ike")
print(person2, type(person2))

# Get values
print(person['first'])
print(person.get('last'))

# Add key value
person['phone'] = '555-555-5555'

# Get dict keys
print(person.keys())

# Get items
print(person.items())

# Copy a dict
person3 = person.copy()

# Remove item
del(person(age))
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))

# List of dict
people = [
    {'first': 'Jake', 'last': 'Ike'},
    {'first': 'Sara', 'last': 'Ike'}
]

print(people)