print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор, 
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.
 
# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50
 
# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.
 
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!
name_customer = input('Введите ваше имя: ')
duty_value = int(input('Введите сумму долга: '))
initial_value_repay = 0
while True:
    print(f'{name_customer}, ваша задолженность составляет {duty_value} рублей.')
    initial_value_repay += int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
    if initial_value_repay >= duty_value:
        print(f'Отлично, {name_customer}! Вы погасили долг. Спасибо!')
        break
    else:
        print(f'Маловато, {name_customer}. Давайте ещё раз.')