"""
Sort a list

Create a function in Python that accepts two parameters.
The first will be a list of numbers. The second parameter will be a string that can be one of the following values: asc, desc, and none.

If the second parameter is “asc,” then the function should return a list with the numbers in ascending order.
If it’s “desc,” then the list should be in descending order, and if it’s “none,” it should return the original list unaltered.
"""


def sorting(numbers, option):
    if option == "asc":
        return sorted(numbers)
    elif option == "desc":
        return sorted(numbers, reverse=True)
    else:
        return numbers


# sort a list without using built-in python functions
def bubble_sorting(numbers, option):
    def asc(arr):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    def desc(arr):
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if arr[j] < arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr

    if option == "asc":
        return asc(numbers)
    elif option == "desc":
        return desc(numbers)
    else:
        return numbers


input_numbers = input('Enter the list of numbers (The numbers should be separated by ","): ')
input_sort = input('Enter the sorting options out of (asc,desc,none): ')

input_numbers_list = [int(num) for num in input_numbers.split(',')]

print(f'The sorted list based on {input_sort} is: {sorting(input_numbers_list, input_sort)}')
print(f'The sorted list based on {input_sort} is: {bubble_sorting(input_numbers_list, input_sort)}')
