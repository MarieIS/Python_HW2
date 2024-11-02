my_num = 11
try_count = 0
success = False
while not success:
    your_num = int(input('Введите ваше число: '))
    if your_num == my_num:
        try_count += 1
        success = True
        print('Количество попыток: ', try_count)
    else:
        try_count += 1