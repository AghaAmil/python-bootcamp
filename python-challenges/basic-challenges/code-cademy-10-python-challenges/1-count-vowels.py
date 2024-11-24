"""
Count Vowels

write a program that get a string, count and return total number of vowels (a, e, i, o, u) in it
print count per each vowel too
"""

# get user's input
user_input = input("Enter a sentence or some texts: ")

counter = 0
vowels = []

# change the user input to lowercase
# therefore A and a both counts as vowel
lower_case = user_input.lower()

for char in lower_case:
    if char in ['a', 'e', 'i', 'o', 'u']:
        counter += 1
        vowels.append(char)

print(f'The Total number of vowels: {counter}')
print(f'The list of vowels: {vowels}')
