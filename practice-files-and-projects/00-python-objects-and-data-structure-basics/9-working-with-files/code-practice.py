# opening a python file
my_file = open('../../sample-python-files/sample-file.txt')

print('The content of the file is displayed below:')
print(my_file.read())

# blank line
print('')

print('Calling the .read() method again will result an empty string:')
print(my_file.read())

# reset cursor
my_file.seek(0)

print('We have reset the position of the contents of the file, we read the file again:')
print(my_file.read())

# blank line
print('')

# reset cursor
my_file.seek(0)

print('Store the content of file line-by-line in a variable and then print it:')
file_content = my_file.readlines()

print(file_content)

my_file.close()

# A different method of opening and extracting the file contents in python without the requirement of closing the file.
print('Display the content of a file using an alternate method:')
with open('../../sample-python-files/sample-file.txt') as new_file_1:
    content = new_file_1.read()

print(content)

# creating a new file using python write() method
with open('../../sample-python-files/sample-file-1.txt', mode='w') as new_file_2:
    new_file_2.write('This file is created using python.\n')
    new_file_2.write('Another line is added, but i do not know what is going to happen :)')

# blank line
print('')
print('The content of the newly created file is displayed below:')

with open('../../sample-python-files/sample-file-1.txt', mode='r') as new_file_2:
    print(new_file_2.read())

# going to append a new line to our file
with open('../../sample-python-files/sample-file-1.txt', mode='a') as new_file_3:
    new_file_3.write('\nThis new line is appended to this file\n')

print('')
print('A new line is appended to the file:')


with open('../../sample-python-files/sample-file-1.txt', mode='r') as new_file_3:
    print(new_file_3.read())

# let's iterate through the lines of a file
with open('../../sample-python-files/sample-file-1.txt', mode='r') as my_file_1:
    content = my_file_1.readlines()

print(content)

print('Let\'s iterate through the a file using loops\n')

for line in open('../../sample-python-files/sample-file.txt'):
    print(line)

# blank line
print('')

# let's test something different
for lines in content:
    print(lines)
