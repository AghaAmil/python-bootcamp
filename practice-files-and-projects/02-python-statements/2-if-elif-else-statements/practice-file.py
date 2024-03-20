"""
Some Python Challenges
"""

"""
Challenge 1: Write a program that asks the user for their age and then prints out a message depending on whether 
they are a child, teenager, adult, or senior citizen.
"""

# take the user's input and convert it into integer
user_age_input = int(input('Please enter your age as an positive integer: '))

if user_age_input < 1:
    print('Please enter a valid number')
elif user_age_input <= 10:
    print('You are a child')
elif 10 < user_age_input <= 18:
    print('You are a teenager')
elif 18 < user_age_input <= 40:
    print('You are an adult')
else:
    print('You are a senior citizen')

# blank line
print('\n')

"""
Challenge 2: Write a program that asks the user for their grade (from 1 to 100) and then prints out a message 
depending on whether they passed or failed. Assume that passing grade is 50.
"""

# take the user's input and convert it into integer
user_grade_input = int(input('Please enter your grade as an integer between 1 and 100: '))

if 0 <= user_grade_input < 50:
    print('You are failed')
elif 50 <= user_grade_input <= 100:
    print('You are passed')
else:
    print('Enter a valid number')

# blank line
print('\n')

"""
Challenge 3: Write a program that asks the user for their favorite color and then prints out a message depending 
on whether they like the color or not. Assume that the only color you like is blue.
"""

user_favorite_color = input('Enter the developer\'s favorite color: ')

if user_favorite_color.lower() == 'blue':
    print('You\'ve guessed it right')
else:
    print('it\'s wrong, Try Again!')
