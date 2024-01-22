# Example 1
counter = 0

while counter <= 5:
    print(f'Iteration no. {counter}')
    counter += 1

print('End of while loop')

# bank lines
print()
print()

# Another example of while loop using input() method
user_input = '0'

while user_input.isnumeric():
    # The isnumeric() function that returns true if input is an integer, false otherwise
    user_input = input('Enter a number: ')
    if user_input.isnumeric():
        print(f'Your input is {user_input}')

print('You have entered an invalid input. End of the while loop.')

# Using else statement in the while loop

counter1 = 0

while counter1 < 5:
    print(f'Iteration no. {counter1}')
    counter1 += 1
else:
    print('While loop over. Now in else block')
print('End of while loop')
