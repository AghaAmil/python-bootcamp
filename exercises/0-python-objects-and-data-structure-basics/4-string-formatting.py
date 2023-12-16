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

