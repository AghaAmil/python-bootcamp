"""
Python Strings Indexing and Slicing

"""

# string indexing
my_string = 'Amirhossein Moravveji'
print('This is a string = ', my_string)
print('The length of the string is: ', len(my_string))
print('The first character of the string is: ', my_string[0])
print('The last character of the string is: ', my_string[-1])
print('The last character of the string using another method is: ', my_string[20])
print('The index of -20 in the string is: ', my_string[-20])
print('The index of -21 (which is the first character) in the string is: ', my_string[-21])

# blank line
print()

# string slicing
my_string_2 = 'This is a string which is going to be sliced :)'
print('Sample String: ', my_string_2)
print('The length of the string is: ', len(my_string_2))
print('Slicing the string [:6]', my_string_2[:6])
print('Slicing the string [11:]', my_string_2[11:])
print('Slicing the string [3:34]', my_string_2[3:34])
print('Slicing the string [3:34:2]', my_string_2[3:34:2])
print('Slicing the string [::]', my_string_2[::])
print('Slicing the string [::2]', my_string_2[::2])
print('Slicing the string [::-1] (string reversed)', my_string_2[::-1])
print('Slicing the string [-9:-4]', my_string_2[-9:-4])