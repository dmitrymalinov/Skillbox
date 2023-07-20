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
current_symbols = 1
for every_row in range(1,pyramid_height+1):
    current_spaces = pyramid_height - every_row
    print(' ' * current_spaces,end = '')
    for every_symbol in range(current_symbols):
        print("#",end = '')
    current_symbols += 2
    print()