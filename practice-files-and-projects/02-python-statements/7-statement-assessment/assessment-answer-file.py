# Question 1
print('Question 1 - Use for, .split(), and if to create a Statement that will print out words that start with ‘s’:')

str_1 = 'Print only the words that start with s in this sentence'
split_str = str_1.split()

for word in split_str:
    if 's' in word[0]:
        print(word, end=', ')

# blank lines
print()
print()

print('Question 2 - Use range() to print all the even numbers from 0 to 10.')

for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=' ')

# blank lines
print()
print()

print('Question 3 - Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.')
list_1 = [num for num in range(1, 50) if num % 3 == 0]
print(list_1)

# blank lines
print()
print()

print('Question 4 - Go through the string below and if the length of a word is even print "even!')

str_2 = 'Print every word in this sentence that has an even number of letters'
split_str_2 = str_2.split()

for word in split_str_2:
    if len(word) % 2 == 0:
        print(word, end=', ')

# blank lines
print()
print()

print('Write a program that prints the integers from 1 to 100. But for multiples of three print “Fizz” instead of the '
      'number, and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five '
      'print “FizzBuzz”.')

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz', end=' ')
    elif num % 3 == 0:
        print('Fizz', end=' ')
    elif num % 5 == 0:
        print('Buzz', end=' ')
    else:
        print(num, end=' ')

# blank lines
print()
print()

print('Question 5 - Use List Comprehension to create a list of the first letters of every word in the string below:')
print('Use List Comprehension to create a list of the first letters of every word in the string below')

str_3 = 'Use List Comprehension to create a list of the first letters of every word in the string below'
split_str_3 = str_3.split()

list_2 = [char[0] for char in split_str_3]
print(list_2)
