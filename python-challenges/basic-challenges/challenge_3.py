"""
Create a simple Rock, Paper, Scissors game using if-elif statements and a for loop. The program should:

1. Play 5 rounds against the computer
2. In each round, ask the user for their choice (Rock, Paper, or Scissors)
3. Generate the computer's random choice
4. Determine the winner using if-elif statements
5. Keep track of wins and losses
6. Print out the final score
"""
import random

player_wins = 0
computer_wins = 0


def game_rules(player, computer):
    global player_wins, computer_wins

    if player == computer:
        return "Draw"
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (
            player == "scissor" and computer == "paper"):
        player_wins += 1
        return "Player Wins!"

    else:
        computer_wins += 1
        return "Computer Wins!"


rounds = int(input('Enter the number of rounds: '))

for i in range(rounds):

    player_choice = input('Choose Rock, Paper, or Scissors: ').lower()

    while player_choice not in ['rock', 'paper', 'scissors']:
        player_choice = input('Invalid input, Please choose Rock, Paper, or Scissors: ').lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f'Player: {player_choice} Vs Computer: {computer_choice}')
    print(game_rules(player_choice, computer_choice))
    print()

print(f'Score - Player: {player_wins}, Computer: {computer_wins}')
print(f'Game Over!')
