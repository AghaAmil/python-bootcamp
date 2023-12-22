# opening a python file
my_file = open('sample-file.txt')

print('The content of the file is displayed below: \n')
print(my_file.read())

# blank line
print('')

print('Calling the .read() method again will result an empty string: \n')
print(my_file.read())

# reset cursor
my_file.seek(0)

print('We have reset the position of the contents of the file, we read the file again: \n')
print(my_file.read())

# blank line
print('')

# reset cursor
my_file.seek(0)

print('Store the content of file line-by-line in a variable and then print it: \n')
file_content = my_file.readline()

print(file_content)

