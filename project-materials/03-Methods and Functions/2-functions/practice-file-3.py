from random import shuffle

# check and test the shuffle function
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(sample_list)

print(sample_list)


# create my own shuffle function
def shuffle_list(l):
    shuffle(l)
    return l


# test the function
print(shuffle_list(sample_list))


def get_user_input():
    user_input = ''

    while user_input not in ['0', '1', '2']:
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
