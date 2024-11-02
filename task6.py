# Ввод количества мальчиков и девочек
boys = int(input('Введите количество мальчиков: '))
girls = int(input('Введите количество девочек: '))

# Инициализация пустой строки для результата
answer = ''

# Проверка возможности корректного распрделения мальчиков и девочек
if (boys > 2 * girls) or (girls > 2 * boys):
    # Если мальчиков или девочек слишком много для корректного чередования
    print('Нет решения')

elif boys >= girls:
    # Если мальчиков больше или их количество равно количеству девочек
    k = boys - girls # Количество лишних мальчиков
    # Вставка лишних мальчиков между девочками
    for bgb in range(k):
        answer += 'BGB'
    # Добавление оставшихся мальчиков и девочек
    for bg in range(girls - k):
        answer += 'BG'

else:
    # Если девочек больше, чем мальчиков
    k = girls - boys # Количество лишних мальчиков
    # Вставка лишних девочек между мальчиками
    for gbg in range(k):
        answer += 'GBG'
    # Добавление оставшихся мальчиков и девочек
    for gb in range(boys - k):
        answer += 'GB'

# Вывод ответа
print(answer)