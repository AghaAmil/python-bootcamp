# Python for-else Loops

for num in range(6):
    print(f'The iteration number is {num}')
else:
    print('Loop interation is over.')
print('End of the loop')

# Blank lines
print('\n')

# Nested loops
for i in range(1, 11):
    for j in range(1, 11):
        multiply = i * j
        print('{:3}'.format(multiply), end=' ')
    print()


