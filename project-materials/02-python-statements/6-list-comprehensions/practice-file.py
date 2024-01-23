# list comprehension
list1 = [x for x in range(11)]
print(list1)

list2 = [x ** 2 for x in range(11)]
print(list2)

list3 = [x ** 2 for x in range(11) if x % 2 == 0]
print(list3)

list4 = [char for char in 'Amirhossein']
print(list4)

# more complex scenarios
celsius = [0, 10, 23.3, 34.11]
print(f'Temperature in Celsius: {celsius}')

fahrenheit = [(9 / 5) * temp + 32 for temp in celsius]
print(f'Temperature in Fahrenheit: {fahrenheit}')

list5 = [x if x % 2 == 0 else 'Odd Number' for x in range(11)]
print(list5)

# not recommended to use this method of list comprehension
list6 = []

for x in [2, 4, 6, 8]:
    for y in [1, 10, 100, 1000]:
        list6.append(x*y)

print(list6)

list7 = [x*y for x in [2, 4, 6, 8] for y in [1, 10, 100, 1000]]
print(list7)




