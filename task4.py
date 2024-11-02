month_count = 0
sum_salary = 0
while month_count != 12:
    month_count += 1
    salary = int(input('Введите свою зарплату: '))
    sum_salary += salary

mean_salary = sum_salary / month_count
print('Средняя зарплата сотрудника равна: ', mean_salary)