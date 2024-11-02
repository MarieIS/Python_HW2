cards_count = int(input('Введите количество карточек: '))
total_sum = 0

for i in range(1, cards_count+1):
    total_sum += i

for i in range(cards_count-1):
    user_card = int(input('Введите номер карты из оставшейся колоды: '))
    total_sum -= user_card

print('Номер потерявшейся карты: ', total_sum)