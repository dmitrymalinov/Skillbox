print('Задача 10.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# 
# Вводится число N,
# далее еще N − 1 чисел: 
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
number_lost_card = 0
card_list = list()
number_of_cards = int(input("Введите количество карточек: "))
for current_card in range(1,number_of_cards):
    last_card = int(input("Введите номер оставшейся карточки: "))
    card_list.append(last_card)
for full_card in range(1,number_of_cards+1):
    if full_card not in card_list:
        number_lost_card = full_card
print(f"Номер пропавшей карточки {number_lost_card}")