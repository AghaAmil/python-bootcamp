from random import randint


def employee_data(fname, lname, id, team='Snapp'):
    """
    This is simple function which print employee details
    :param fname: employee first name
    :param lname: employee last name
    :param id: employee id
    :param team: employee team
    :return:
    """
    print(f'The Employee Full Name Is: {fname} {lname}')
    print(f'The Employee ID Is: {id}')
    print(f'The Employee Team Is: {team}\n(Note: If the employee team is not determined yet, the default team is '
          f'selected)')


employee_data('Amirhossein', 'Moravveji', 7868, 'QA Team')

# blank line
print()

employee_data('Ali', 'Behnam', 22003)

# blank line
print()
print()


# the differences between return and print
def function_with_return(num1, num2):
    return num1 + num2


def function_with_print(num1, num2):
    print(num1 + num2)


print('Check the written code to understand the difference.')
# assign the return value to a variable
result = f'The returned value is: {function_with_return(10, 20)}'
print(result)

# assigning the printed value to a variable is not possible
# result = function_with_print(10, 20)
print('The printed value is: ', end='')
function_with_print(10, 20)

# blank line
print()
print()

# let's try a more advanced example

# let's generate a list of random numbers from 1 to 100
list_of_numbers = []

for i in range(15):
    list_of_numbers.append(randint(1, 100))

print(f'This is a list of random numbers: {list_of_numbers}')


def check_even_odd_func(list_numbers):
    """
    This function returns a separated list of even and odd numbers
    This is a bit advance function
    :param list_numbers: input list of number
    :return: the separated list of even and odd numbers
    """
    even_numbers = []
    odd_numbers = []

    for nums in list_numbers:
        if nums % 2 == 0:
            even_numbers.append(nums)
        else:
            odd_numbers.append(nums)

    even_numbers_list = f'The list of even numbers: {even_numbers}'
    odd_numbers_list = f'The list of odd numbers: {odd_numbers}'

    return even_numbers_list, odd_numbers_list


result = check_even_odd_func(list_of_numbers)
print(result)
print(type(result))
