# Using "for" with a String
print("A string is a sequence of Unicode letters, each having a positional index.\n"
      "The following example compares each character and displays if it is not a vowel ('a', 'e', 'I', 'o' or 'u')")

zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''

print(zen)

for letter in zen:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        # ends the print output with no space
        # letter will be printed side by side
        print(letter, end='')

# print blank lines
print('\n')

# Using "for" with a Tuple
print('Print the sum of the values in the tuple below using for loop:')

numbers = (34, 54, 67, 21, 78, 97, 45, 44, 80, 19)
print(numbers)

sum = 0

for nums in numbers:
    sum += nums

print(f'The sum of the numbers in the tuples is: {sum}')

# Using "for" with a Range Object
sample_num = range(5)
print(list(sample_num))

sample_num2 = range(10, 20)
print(list(sample_num2))

sample_num3 = range(1, 10, 2)
print(list(sample_num3))

# Using 'for' loop
for num in range(5):
    print(num, end=' ')
print('')

for num in range(10, 20):
    print(num, end=' ')
print('')

for num in range(1, 10, 2):
    print(num, end=' ')

# blank lines
print('\n')
print('We use the range() function to get the sequence of numbers from 1 to n-1 and perform cumulative '
      'multiplication to get the factorial value.')

fact = 1
n = 5

for num in range(1, n + 1):
    fact *= num

print(f'The factorial of 5! = {fact}')

# blank lines
print('\n')

# Using "for" Loop with Sequence Index
sample_num4 = [34, 54, 67, 21, 78, 45, 12]
range_value = range(len(sample_num4))

for items in range_value:
    print(f'The Index: {items}, Number: {sample_num4[items]}')

# blank lines
print('\n')

# Using "for" with Dictionaries
numbers = {10: "Ten", 20: "Twenty", 30: "Thirty", 40: "Forty"}
print(numbers)

for x in numbers:
    print(f'{x} : {numbers[x]}')
