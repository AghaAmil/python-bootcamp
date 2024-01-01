# formatting with placeholders (old method, not recommended)
print('Hi, my name is %s' % 'amirhossein')
print('This is an another example. my %s' % 'pashmzz')
print('You can use %s %s using this method' % ('multiple', 'injections'))

# inject a variable
my_full_name = 'Amirhossein Moravveji'

print('my full name is %s' % my_full_name)

# blank line
print('')

# Format conversion methods
# let's check the difference
print('Hi there, my name is %s' % my_full_name)
print('Hi there, my name is %r' % my_full_name)

# blank line
print('')

# another example when inserting a tab
print('This is something new in %s' % 'Python \t Language')
print('This is something new in %r' % 'Python \t Language')

# blank line
print('')

# consider the %d
print('The number PI in mathematics is equal to %s' % 3.14)
print('The number PI in mathematics is equal to %d' % 3.14)

# blank line
print('')

# Padding and Precision of Floating Point Numbers
print('This is a float number: %4.2f' % 34.1555)
print('This is a float number: %5.2f' % 34.1555)
print('This is a float number: %6.2f' % 34.1555)
print('This is a float number: %10.2f' % 34.1555)
print('This is a float number: %5.4f' % 34.1555)
print('This is a float number: %.4f' % 34.1555)
print('This is a float number: %.0f' % 34.1555)
print('This is a float number: %1.0f' % 34.1555)

# blank line
print('')

# multiple formatting
print('First: %s, Second: %5.2f, Third: %r,' % ('number', 77.123, 'COOL'))

# blank line
print('')

# Formatting with the .format() method
print('Hello, My name is {}'.format('amirhossein'))
print('Hello, My complete name is {} {}'.format('Amirhossein', 'Moravveji'))

user_name = 'kecy1amr'
print('My user name is {}'.format(user_name))

print('The {} {} {}'.format('fox', 'brown', 'quick'))
print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))
print('The {q} {b} {f}. The {q} red {f}'.format(f='fox', b='brown', q='quick'))

# blank line
print('')

print('{0:8} | {1:9}'.format('Fruits', 'Quantity'))
print('{0:8} | {1:9}'.format('Apple', 3.))
print('{0:8} | {1:9}'.format('Orange', 10))

# blank line
print('')

print('{0:<10} | {1:^10} | {2:>10}'.format('Left', 'Center', 'Right'))
print('{0:<10} | {1:^10} | {2:>10}'.format(11, 22, 33))

# blank line
print('')

print('{0:=<10} | {1:-^10} | {2:.>10}'.format('Left', 'Center', 'Right'))
print('{0:=<10} | {1:-^10} | {2:.>10}'.format(11, 22, 33))

# blank line
print('')

# decimal numbers using .format()
print('This is my tenth character, two-decimal number %10.2f' % 45.778)
print('This is my tenth character, two-decimal number {0:10.2f}'.format(45.778))

# blank line
print('')

# Formatted String Literals (f-strings)
print(f'My full name is : {my_full_name}')
print(f'My first name is : {my_full_name!r}')

num = 12.778983
print(f'The result of the calculation is equal to : {num:{15}.{3}}')
print(f'The result of the calculation is equal to : {num:{10}.{6}}')
print(f'The result of the calculation is equal to : {num:.{6}}')

# use .format() method syntax inside an f-string
print(f'The result of the calculation is equal to : {num:10.3f}')
