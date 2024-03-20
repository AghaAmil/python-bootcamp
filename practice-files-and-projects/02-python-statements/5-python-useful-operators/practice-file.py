# import functions
from random import randint, shuffle

# range function
print('1. Range Function')
print(list(range(1, 20, 2)))

# blank line
print()

# enumerate function
print('2. Enumeration Function')
counter = 0
myName = 'Amirhossein'

for char in myName:
    print(f'In the index {counter}, we have letter: {char}')
    counter += 1

# blank line
print()

for letters in enumerate(myName):
    print(letters)

# using tuples unpacking
for index, letter in enumerate(myName):
    print(f'At the index {index}, the letter is {letter}')

# blank line
print()

print('3. Zip Function')
list1 = [1, 2, 3, 4]
list2 = ['Tehran', 'Karaj', 'Damavand']
list3 = ['a', 'b', 'c']

zipped_list = zip(list1, list2, list3)
print(zipped_list)
print(list(zipped_list))

# use loop to generate the result of the zip function
for x, y, z, in zip(list1, list2, list3):
    print(f'The first element is "{x}" and the second element is "{y}" and the third element is "{z}"')

# blank line
print()

# In operator
print('4. In Operator')

print('x' in 'Xtronic')
print('X' in 'Xtronic')
print('x' in [1, 2, 3, 4, 5])
print('5' in [1, 2, 3, 4, 5])
print(5 in [1, 2, 3, 4, 5])

print('x' not in ['x', 'y', 'z'])
print('x' not in [1, 2, 3])

# blank line
print()

# min() & max() functions
print('5. Min & Max Functions')

myList = range(10, 110, 10)
print(list(myList))

print(max(myList))
print(min(myList))

# blank line
print()

print('6. Random Function - Shuffle')

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sample_list)

shuffle(sample_list)
print(sample_list)

# blank line
print()

print('7. Random Function - Randint')
print('Print a random integer between 0 and 100')
print(randint(0, 100))
