# create a dictionary
user_info = {
    'first_name': 'Amirhossein',
    'last_name': 'Moravveji',
    'age': 30,
    'position': 'Senior QA Engineer',
    'location': 'San Francisco'
}

print(user_info)

# blank line
print('')

print(type(user_info))

print(user_info['first_name'])
print(user_info['last_name'])
print(user_info['age'])
print(user_info['position'])
print(user_info['location'])

# blank line
print('')

# dictionary with different item types
my_dick = {
    'key1': 'string value',
    'key2': 12.34,
    'key3': [1, 2, 3, 'a', 'b'],
    'key4': {
        'inner_key1': 'inner_key1_value',
        'inner_key2': 33
    }
}

print(my_dick)

print(my_dick['key3'])
print(my_dick['key3'][2])
print(my_dick['key3'][3])
print(my_dick['key4']['inner_key1'])
print(my_dick['key4']['inner_key2'])

print(my_dick['key3'][3].upper())
print(my_dick['key3'][4].upper())

my_dick['key5'] = [[1, 2], [1, 2]]
print(my_dick)

my_dick['key2'] += 43.21
print(my_dick['key2'])

# blank line
print('')

# create an empth dictionary and add the key:value pair later
empty_dick = {}

empty_dick['name'] = 'Amirhossein'
empty_dick['last_name'] = 'Moravveji'

print(empty_dick)

# blank line
print('')

# Method to return a list of all keys
print(user_info.keys())

# Method to return a list of all values
print(user_info.values())

# Method to return tuples of all items
print(user_info.items())

