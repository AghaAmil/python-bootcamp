# let's make an *args example
def averager(*args):
    print(args)
    print(type(args))

    sum = 0

    for nums in args:
        sum += nums

    return sum / len(args)


print(averager(1, 2, 3, 4, 5, 6, 76, 7, 10))

# blank line
print()


# let's make a *kwargs example
def meal(**kwargs):
    print(kwargs)
    print(type(kwargs))

    if 'food' in kwargs:
        print('The today\'s lunch: {}'.format(kwargs['food']))
    else:
        print('lunch is not ready')


meal(drink='Cola', food='Sandwich', dessert='Ice Cream')

# blank line
print()


# mix of *args and **kwargs
def myfunc(*args, **kwargs):
    if 'fruit' and 'juice' in kwargs:
        print(f"I like {' and '.join(args)} and my favorite fruit is {kwargs['fruit']}")
        print(f"May I have some {kwargs['juice']} juice?")
    else:
        pass


myfunc('eggs', 'ham', 'sausage', fruit='cherries', juice='orange')
