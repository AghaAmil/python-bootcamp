"""
String Methods

"""

name = 'amirhossein moravveji'
name_cap = 'AMIRHOSSEIN MORAVVEJI'
text = 'good morning! my name is amirhossein moravveji.'
text_2 = 'Hello World! Welcome to the Python.'
text_3 = 'Hi there, this is a string.'
text_4 = 'banana,orange,apple,carrot'


# lowercase
print(name_cap)
print(name_cap.lower())

# blank line
print()

# uppercase
print(name)
print(name.upper())

# blank line
print()

# capitalize
print(text)
print(text.capitalize())

# blank line
print()

# split
print(text_2)
print(text_2.split())

# blank line
print()

print(text_3)
print(text_3.split('i'))

# blank line
print()

print(text_4)
print(text_4.split(','))