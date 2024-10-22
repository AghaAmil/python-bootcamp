"""
Convert radians into degrees

Write a function in Python that accepts one numeric parameter.
This parameter will be the measure of an angle in radians.
The function should convert the radians into degrees and then return that value.

While you might find a Python library to do this for you, you should write the function yourself.
One hint you get is that you’ll need to use Pi in order to solve this problem. You can import the value for Pi from Python’s math module.
"""
import math


def angel_change(angel):
    angel_degrees = (angel * 180) / math.pi
    return angel_degrees


while True:
    try:
        angel_radian = float(input('Enter the angle in radians: '))
        print('Angel In Degrees: {:.3f}'.format(angel_change(angel_radian)))
        break

    except ValueError:
        print('Please enter a numeric number.')
