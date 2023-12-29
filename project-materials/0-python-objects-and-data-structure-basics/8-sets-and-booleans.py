# let's create a set
my_set = set()

print(my_set)

my_set.add(1)
my_set.add(2)
my_set.add(4)

print(my_set)

# add another repetitive number
my_set.add(4)

print(my_set)

# add another unique object to our set
my_set.add(3)

print(my_set)

my_list = [1, 1, 1, 2, 3, 4, 5, 4, 4, 4, 5, 6, 4, 3, 3, 2, 4, 3, 4]
print(my_list)
print(set(my_list))

# convert a string into a set of unique characters
string_1 = 'Amirhossein'
print(set(string_1))

# blank line
print('')

# booleans
a = True
b = False

print(a)
print(b)

print(type(a))
print(type(b))

# We can use None as a placeholder for an object that we don't want to reassign yet:
none_variable = None
print(none_variable)
print(type(none_variable))
