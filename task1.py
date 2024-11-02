pos_count = 0
neg_count = 0

number = int(input('Введите число: '))

while number != 0:
    if number > 0:
        pos_count +=1
    else:
        neg_count +=1
    number = int(input('Введите число: '))

print('Количество положительных чисел равно: ', pos_count)
print('Количество отрицательных чисел равно: ', neg_count)