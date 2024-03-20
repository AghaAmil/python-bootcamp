employee_working_hours = [('Amir', 34), ('Ali', 28), ('Jack', 44), ('John', 32), ('Jeff', 38)]


def hard_worker(employee_list):
    current_max = 0
    winner_employee = ''

    for employee, hour in employee_list:
        if hour > current_max:
            current_max = hour
            winner_employee = employee
        else:
            pass

    return winner_employee, current_max


# print(hard_worker(employee_working_hours))
name, working_hours = hard_worker(employee_working_hours)
print(f'The most hard working employee is "{name}" with "{working_hours}" working hours.')