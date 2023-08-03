print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. 
# Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
pit_height = int(input("Введите высоту ямы: "))
current_dots = 0
for every_row in range(pit_height):
    for every_column in range(every_row + 1):
        current_symbol_to_print = pit_height - every_column
        print(current_symbol_to_print,end='')
    current_dots = pit_height - (every_column + 1)
    print('.' * current_dots,end = '')
    for every_column in range(1,pit_height+1):
        if every_column <= pit_height - (every_row+1):
            print('.',end = '')
        else:
            print(every_column,end='') 
    print()
   