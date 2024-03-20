from random import shuffle

# check and test the shuffle function
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Original list: {sample_list}')

shuffle(sample_list)
print(f'Shuffled list: {sample_list}')


# create my own shuffle function
def shuffle_list(l):
    shuffle(l)
    return l


# test the function
# in this situation we can assign the result of the shuffle function to a variable
mixed_list = shuffle_list(sample_list)

print(f'Creating my own shuffle function: {mixed_list}')

# blank line
print()


def get_user_input():
    user_input = ''

    while user_input not in ['0', '1', '2']:
        print('Please enter a valid number below:')
        user_input = input("Choose a number from 0, 1, or 2: ")

    return int(user_input)


def game_result(input_list, guess):
    if input_list[guess] == 'O':
        print('You won!, Guess it right!')
        print(input_list)
    else:
        print('You lost!, Guess it wrong!')
        print(input_list)


# INITIAL LIST
initial_list = [' ', 'O', ' ']

# SHUFFLE LIST
shuffle_list(initial_list)

# TAKE USER'S GUESS
user_guess = get_user_input()

# CHECK THE RESULT
game_result(initial_list, user_guess)
