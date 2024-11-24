"""
Are the Xs equal to the Os?
Create a Python function that accepts a string.
This function should count the number of Xs and the number of Os in the string.
It should then return a boolean value of either True or False.

If the count of Xs and Os are equal, then the function should return True.
If the count isn’t the same, it should return False. If there are no Xs or Os in the string, it should also return True because 0 equals 0.
The string can contain any type and number of characters.
"""


def string_checker(text):
    text = text.lower()
    if text.count('x') == text.count('o'):
        return True
    return False


user_input = input("Enter a string (can contain any type and number of characters): ")

if string_checker(user_input):
    print('The count of Xs and Os is equal')
else:
    print('The count of Xs and Os is NOT equal')
