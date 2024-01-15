# Using "for" with a String
print("A string is a sequence of Unicode letters, each having a positional index.\n"
      "The following example compares each character and displays if it is not a vowel ('a', 'e', 'I', 'o' or 'u')")

zen = '''
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
'''

print(zen)

for letter in zen:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u']:
        # ends the print output with no space
        # letter will be printed side by side
        print(letter, end='')
