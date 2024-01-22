# Let's see some simple examples

for letter in "Python":
    if letter == "h":
        break

    print(f'The letters in python are: {letter.lower()}')

print('Loop is broken when reached letter "h"')

# Blank Lines()
print()
print()

# Another example with while
counter = 10

while counter > 0:
    if counter == 5:
        break

    print(f'The counter is: {counter}')
    counter -= 1

print('Loop is broken when reached number "5"')
