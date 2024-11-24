"""
Create a calculator function
Write a Python function that accepts three parameters.
he first parameter is an integer.
The second is one of the following mathematical operators: +, -, /, or *.
The third parameter will also be an integer.

The function should perform a calculation and return the results.
For example, if the function is passed 6 and 4, it should return 24.
"""

userinput_1 = float(input("Enter you first number: "))
input_operator = input("Enter mathematical operators: +, -, /, or *: ")

while input_operator not in ['+', '-', '/', '*']:
    print("Invalid input. Please try again.")
    input_operator = input("Enter mathematical operators: +, -, /, or *: ")

userinput_2 = float(input("Enter you second number: "))


def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


# return the result of the operation as simple integer if the value is not a float
# display 7.0 as 7
def format_number(number):
    if number.is_integer():
        return int(number)
    return


if input_operator == "+":
    result = addition(userinput_1, userinput_2)
    print(result)
elif input_operator == "-":
    result = subtraction(userinput_1, userinput_2)
    print(result)
elif input_operator == "/":
    result = division(userinput_1, userinput_2)
    print(result)
elif input_operator == "*":
    result = multiplication(userinput_1, userinput_2)
    print(result)
else:
    print("Invalid Input Operator")
