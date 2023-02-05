# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Create dict
person = {
    'first_name': 'Farha',
    'last_name': 'Djama',
    'age': 19
}
# Use constructor
# person2 = dict(first_name='Sara', last_name='Williams')
# Get value
print(person['first_name'])
print(person.get('last_name'))
# Add key/value
person['phone'] = '555-555-5555'
# Get dict keys
print(person.keys())
# Get dict items
print(person.items())
# Copy dict
person2 = person.copy()
person2['city'] = 'Boston'
# Remove item
del(person2['age'])
person.pop('phone')
# Clear
person.clear()
# Get length
print(len(person2))
# List of dict
person = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]
print(person[1]['name'])