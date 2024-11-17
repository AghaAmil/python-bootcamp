"""
Hide the credit card number

Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent “4444444444444444”, then it should return “4444”.

I'm going to add some extra validation and functionality.
credit card number should be 16 digits

# Part 2:
Sample input: 1234123412341234
Sample output: 1234 **** **** 1234
"""


def encrypter(number):
    # Convert the string to a list as strings are immutable
    number = list(number)

    for index in range(len(number) - 4):
        number[index] = '*'

    # Convert back to string and return
    return ''.join(number)


def encrypter_2(number):
    mask = number[:4] + " **** **** " + number[-4:]
    return mask


ccn = input("Enter a Credit Card Number: ")

while len(ccn) != 16 or not ccn.isdigit():
    print("Invalid input. Please enter a valid 16-digit credit card number.")
    print()
    ccn = input("Enter a Credit Card Number: ")

print(f'The encrypted Credit Card Number is {encrypter(ccn)}')
print(f'The masked Credit Card Number is {encrypter_2(ccn)}')
