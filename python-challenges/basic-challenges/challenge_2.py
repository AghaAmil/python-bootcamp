"""
### Challenge 2: Prime Number Generator

Write a program that generates prime numbers up to a given limit using a for loop and if-elif statements. The program should:

1. Ask the user for the upper limit
2. Use a for loop to iterate from 2 to the limit
3. For each number, check if it's prime using if-elif statements
4. Print out all prime numbers found
"""


def prime_checker(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num + 1):
            if num % i == 0:
                return False
            else:
                return True


number_limit = int(input('Enter the upper limit: '))
primes_container = []

for num in range(2, number_limit + 1):
    if prime_checker(num):
        primes_container.append(num)

print(f'List of the Prime Numbers up to {number_limit}: {primes_container}')
