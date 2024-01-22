# Let's see some simple examples

for letter in "Python":
    if letter == "h":
        continue
    print(f'The letters in python are: {letter.lower()}')

print('The letter "h" is skipped in the loop')

# blank lines
print()
print()

counter = 10

while counter > 0:
    counter -= 1
    if counter == 5:
        continue
    print(f'The counter is: {counter}')


print('The counter "5" is skipped in the loop')