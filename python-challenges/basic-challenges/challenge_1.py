"""
### Challenge 1: Grade Calculator

Create a program that calculates grades for students using nested if-elif statements and a for loop. The program should:

1. Ask the user for the number of students
2. For each student, ask for their name and score
3. Use nested if-elif statements to determine the grade based on the score (A=90-100, B=80-89, C=70-79, D=60-69, F below 60)
4. Print out each student's name and grade as a list

Bonus: write the code in the most efficient and elegant way possible.
"""
from pycparser.c_ast import Return


def scoring(student_score):
    if 90 <= student_score <= 100:
        return "A"
    elif 80 <= student_score <= 89:
        return "B"
    elif 70 <= student_score <= 79:
        return "C"
    elif 60 <= student_score <= 69:
        return "D"
    elif 0 < student_score <= 59:
        return "F"
    else:
        return 'Invalid Grade'


count_student = int(input('Enter the number of students: '))
student_list = []

for i in range(count_student):
    student_name = input(f'Enter student number {i+1} name: ')
    student_score = float(input(f'Enter student number {i+1} score: '))

    scoring(student_score)
    student_list.append([student_name, student_score])

# blank line
print()

print('List of the students with respective levels')
print('*******************************************')
for name, score in student_list:
    print(f'{name}: {scoring(score)} Level Student')







