task_count = 0
task_sum = 0
go_to_store = False
i = 0
while i != 8:
    i += 1
    task_count = int(input('Сколько задач выполнил Максим за этот час?'))
    task_sum += task_count
    get_call = int(input('Звонит жена. Взять трубку?'))
    if get_call == 1:
        go_to_store = True

print('Рабочий день закончился. Всего выполнено задач: ', task_sum)
if go_to_store:
    print('Нужно зайти в магазин')