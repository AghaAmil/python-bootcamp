# Sample of a while loop

x = 0
sum = 0

while x < 10:
    print(f'The current value of x is {x}')
    sum += x
    print(f'The sum of displayed numbers are {sum} ')
    x += 1

# two blank line
print()
print()

"""
Break
Continue
Pass
"""

# continue
for nums in range(0, 20):
    if nums % 2 == 0:
        continue

    print(nums, end=' ')

# blank lines
print()
print()

start_num1 = 0

while start_num1 < 10:
    print('starting number is currently: ', start_num1)
    print('starting number is still less than 10, adding 1 to x')
    start_num1 += 1
    if start_num1 == 3:
        print('The start number is equal to 3')
    else:
        print('continuing...')
        continue

# blank line
print()

# break
for nums in range(0, 20):
    if nums == 10:
        break

    print(nums, end=' ')

# blank line
print()

# pass
for char in 'abcdefghij':
    # some code
    pass

print('That\'s the end of the script')
