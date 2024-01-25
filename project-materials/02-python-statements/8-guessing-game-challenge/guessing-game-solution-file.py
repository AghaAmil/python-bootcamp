from random import randint

print("WELCOME TO GUESS ME!")
print("The game will chose a number between 1 to 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

print()
print()

game_random_num = randint(1, 100)
user_guess_list = [0]

while True:
    user_input = int(input("A number between 1 and 100 is chosen by the game.\nTry guess the number: "))

    if user_input < 1 or user_input > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue

    if user_input == game_random_num:
        print(f'\nCONGRATULATIONS, YOU GUESSED IT IN ONLY {len(user_guess_list)} GUESSES!!')
        break

    user_guess_list.append(user_input)

    if user_guess_list[-2]:
        if abs(game_random_num - user_input) < abs(game_random_num - user_guess_list[-2]):
            print('WARMER!')
        else:
            print('COLDER!')

    else:
        if abs(game_random_num - user_input) <= 10:
            print('WARM!')
        else:
            print('COLD!')
