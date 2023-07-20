print('Задача 7. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

pyramid_height = int(input("Введите высоту пирамиды: "))
current_symbols = 0
odd_number = 1
for every_row in range(1,pyramid_height+1):
    current_spaces = pyramid_height - every_row
    if every_row == 0 :
        current_symbols += 1
    else:
        current_symbols += 2
    for every_space in range(current_spaces):
        print('\t', end='')
    for every_symbol in range(current_symbols):
        if every_row == 0:
            print(odd_number,end = '')
            odd_number +=2
        else:
            if (every_symbol + 1) % 2 == 1:
                print(odd_number,end = '')
                odd_number +=2
            else:
                print('\t' * 2,end = '')
    print()