# creating a tuple
my_tuple = (1, 2, 3, 4)

print(my_tuple)
print(len(my_tuple))

print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])
print(my_tuple[3])
print(my_tuple[-1])

# tuples are immutable
# print(my_tuple[0]) = 10       will cause an error

# blank line
print('')

my_tuple_2 = ('a', 'a', 'b', 'a', 'b', 'b', 'c')
print(my_tuple_2)

# Use .count to count the number of times a value appears
print(my_tuple_2.count('a'))

# # Use .index to enter a value and return the index
print(my_tuple_2.index('a'))
print(my_tuple_2.index('b'))
print(my_tuple_2.index('c'))



