task_count = 0
go_to_store = False
i = 1
while i < 9:
    task_count += i
    get_call = int(input('Звонит жена. Взять трубку?'))
    if get_call == 1:
        go_to_store = True
    i += 1

print('Рабочий день закончился. Всего выполнено задач: ', task_count)
if go_to_store == True:
    print('Нужно зайти в магазин')