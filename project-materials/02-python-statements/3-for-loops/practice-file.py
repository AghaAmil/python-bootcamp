"""
Python For Loop
"""

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
