# creating lists
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample_list_2 = ['AMIR', 199, 23.54]

print(sample_list)
print(sample_list_2)

# blank line
print('')

# type of list
print(type(sample_list))

# blank line
print('')

# length of a list
print(len(sample_list))
print(len(sample_list_2))

# blank line
print('')

# indexing and slicing lists
print(sample_list_2[0])
print(sample_list_2[1])
print(sample_list_2[2])

print(sample_list[3:])
print(sample_list[:6])
print(sample_list[4:9])
print(sample_list[::-1])

# blank line
print('')

# concatenation
sample_list_3 = ['one', 'two', 'three', 'four']
print(sample_list_3 + [5, 6])

new_concat_list = sample_list_3 + [5, 6]
print(new_concat_list)

# update a list
new_concat_list[4] = 'five'
print(new_concat_list)

# make the double
print(sample_list_3 * 2)

# blank line
print('')

# basic list methods
new_concat_list.append('seven')
print(new_concat_list)

print(new_concat_list.pop(-2))
print(new_concat_list)

# blank line
print('')

sample_list_4 = ['x', 'g', 'i', 'b', 'e', 'w', 't']
print(sample_list_4)

sample_list_4.sort()
print(sample_list_4)

# blank line
print('')

sample_list_5 = [2, 12.4, 1, 42, 46, 9, 19, 100, 12]
print(sample_list_5)

sample_list_5.sort()
print(sample_list_5)

sample_list_5.reverse()
print(sample_list_5)

# blank line
print('')

# nesting list
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

matrix = [lst_1, lst_2, lst_3]

print(matrix)

matrix_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

print(matrix_1)

print(matrix_1[0][0])
print(matrix_1[1][1])
print(matrix_1[2][2])

# list comprehension
"""
Lists comprehension will be explained later
"""
