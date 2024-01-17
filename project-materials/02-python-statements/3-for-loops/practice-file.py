"""
Python For Loop
"""
# iterate through the lists
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for nums in my_list:
    # ends the print output with a space
    # numbers will be printed with a space between them
    print(nums, end=' ')

# print two blank lines
print('\n')

for nums in my_list:
    if nums % 2 == 0:
        print(f'{nums} is even')
    else:
        print(f'{nums} is odd')

# print a blank line
print('')

print('This is my list of numbers: ')
print(my_list)

sum = 0

for nums in my_list:
    sum += nums

print(f'The sum of numbers in the list is equal to {sum}')

# print two blank lines
print('\n')

# iterate through the strings
print('The characters in the string below is iterated using for loop and each character is separated by a colon')

sample_string = 'This is a sample string'
print(f'Our Sample String: {sample_string}')

for char in sample_string:
    print(char, end=', ')

# print two blank lines
print('\n')

# iterate through tuples
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for items in tup:
    print(items)

# blank line
print('')

# unpacking tuples
list_tupes = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for items in list_tupes:
    print(items)

print('Unpacking Tuples')

for x, y, z in list_tupes:
    print(x, y, z)

# print two blank lines
print('\n')

# iterate through dictionaries
dic = {
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4
}

for keys in dic:
    print(keys)

print('printing dictionary items')

for keys in dic:
    print(dic.items())

print('dictionary keys and values')

for key, value in dic.items():
    print(key, value, end='\t')

# blank line
print('')

# there is an alternate way to display keys and values of a dictionary
print(list(dic.keys()))
print(list(dic.values()))