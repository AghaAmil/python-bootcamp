"""
String Formatting

"""

# string format operator %
name = 'Amirhossein Moravveji'
age = 30

print('My name is %s and I\'m %d years old' % ('Mahdi Sadeghnia', 26))
print('My name is %s and I\'m %d years old.' % (name, age))

# format conversion methods
# check the differences by running the code
print('My name is %r and I\'m %d years old.' % (name, age))

# blank line
print()

# let's check another exam
print('This is a paragraph ... having %s' % 'some \ttext')
print('This is a paragraph ... having %r' % 'some \ttext')

# blank line
print()

x, y = 'text_1', 'text_2'
print('The position of %s is here, and the position of %s is there' % (x, y))

# blank line
print()

# specifying Width/Padding using % operator
a, b, c = 1, 11, 111
print('a=%5s and b=%5s and c=%5s' % (a, b, c))

# blank line
print()

num1 = 3.14556
num2 = 45.242

print('The number one is %.4f and the number two is %10.2f' % (num1, num2))

# some more examples:
print('Floating point numbers: %1.0f' % 13.144)
print('Floating point numbers: %1.5f' % 13.144)
print('Floating point numbers: %10.2f' % 13.144)
print('Floating point numbers: %25.2f' % 13.144)

# blank line
print()

# string formatting using format() method
# using above variables
print('This is my name: {}'.format(name))
print('This is my age: {}'.format(age))

# blank line
print()

# another example
print('Hello {} {} {}'.format('fox', 'brown', 'quick'))
print('Hello {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('Hello {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
print('Username = {un}'.format(un='#005334'))

# blank line
print()

# alignment, padding and precision using format() method
print('| {0:10} | {1:10} |'.format('Food', 'Quantity'))
print('| {0:10} | {1:10} |'.format('Apple', 3.0))
print('| {0:10} | {1:10} |'.format('Banana', 4.0))
print('| {0:10} | {1:10} |'.format('Orange', 10))

# blank line
print()

# change the alignment
print('| {0:<12} | {1:^12} | {2:>12} |'.format('Left', 'Center', 'Right'))
print('| {0:<12} | {1:^12} | {2:>12} |'.format(10, 20, 30))
print('| {0:<12} | {1:<12} | {2:<12} |'.format(11, 22, 33))
print('| {0:>12} | {1:>12} | {2:>12} |'.format(12, 24, 36))
print('| {0:=<12} | {1:-^12} | {2:.>12} |'.format(13, 26, 39))

# blank line
print()

# float precision
print('This is my ten-character, two-decimal number:%10.2f' % 13.579)
print('This is my ten-character, two-decimal number:{0:10.2f}'.format(13.579))
print('This is a number: {:.3f}'.format(134.553423))

# blank line
print()

# formatted string literals (f-strings)
print(f'This is my name: {name}')
print(f'This is my age: {age}')
print(f'To get the string representation of {name!r}')

# blank line
print()

# evaluate expressions using f-Strings
fruit_one = 10
fruit_two = 20

print(f'We have {fruit_one} Apples and {fruit_two} Oranges. In total We have {fruit_one + fruit_two} fruits.')

# blank line
print()

# precision
num = 24.53
print("My 10 character, four decimal number is: {:10.4f}".format(num))
print(f"My 10 character, four decimal number is: {num:{10}.{4}}")
print(f"My 10 character, four decimal number is: {num:10.4f}")





