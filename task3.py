my_num = 11
try_count = 0
success = False
while not success:
    your_num = int(input('Введите ваше число: '))
    try_count += 1
    if your_num == my_num:
        success = True
        print('Количество попыток: ', try_count)
    else:
        success = False