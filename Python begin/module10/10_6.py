print('Задача 6. Пирамидка')


# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######
pyramid_height = int(input("Введите высоту пирамиды: "))
current_symbols = 0
for every_row in range(pyramid_height):
    current_spaces = pyramid_height - (every_row + 1)
    if every_row == 0 :
        current_symbols += 1
    else:
        current_symbols += 2
    for every_space in range(current_spaces):
        print(' ',end='')
    for every_symbol in range(current_symbols):
        print("#",end = '')
    print()