# creating a new string

print('Hello World!')
print("creating a string using double quote")
print("I'm Amirhossein Moravveji")

# blank line
print("")

# break line
print('This is the first line\nThis is the second line')
print('This is the third line')
print('Check the code to see the differences between them\n')

# using tab between two words
print('Amir \t Moravveji \t')

# print length of the string
print(len('Hello World!'))

# blank line
print("")

# string indexing
string_1 = 'Amirhossein Moravveji'
print(string_1)
print(len(string_1))

# first letter
print(string_1[0])
# last letter
print(string_1[20])  # last index/letter = len(variable) - 1  --> 21 - 1 = 20
print(string_1[-1])  # another way to get last index/letter
# something in between
print(string_1[6])

# string slicing

# starting from an index all the way to the end
print(string_1[3:])
# staring from the beginning all the way to a specific index
print(string_1[:14])  # note that the last index is not included
# selecting a range of indexes
print(string_1[4:11])

# include steps from beginning to the end
print(string_1[::2])
print(string_1[::3])

print(string_1[2:15:2])

# using a python trick the reverse the string
print(string_1[::-1])

# blank line
print("")

# another example
string_2 = 'abcdefghijklmnopqrst'
print(string_2)
print(string_2[::-1])

# blank line
print("")

# string concatenation
x = 'Ali Behnam Manesh'
print(x)

some_of_x = x[4:]
print(some_of_x)

x = 'Youness ' + some_of_x
print(x)

# blank line
print("")

# string multiplication
string_3 = 'abc'
print(string_3)
print(string_3 * 5)

# blank line
print("")

# build-in string methods
my_name = 'Amirhossein Moravveji'
print(my_name)
print(my_name.upper())
print(my_name)              # upper() does not change the variable itself

my_name = my_name.upper()
print(my_name)

print(my_name.lower())
print(my_name)              # lower() does not change the variable itself

# blank line
print("")

custom_string = 'Hello World! Welcome to the Python programming language!'
print(custom_string)

print(custom_string.split())
print(custom_string.split('W'))

custom_string_1 = 'Hi, this is a string'
print(custom_string_1)
print(custom_string_1.split('i'))

# string interpolation
