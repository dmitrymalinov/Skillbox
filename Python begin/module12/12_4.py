print('Задача 4. Число наоборот')

# Вводится последовательность чисел,
# которая оканчивается нулём.
#
# Реализуйте функцию,
# которая принимает в качестве аргумента каждое число,
# переворачивает его и выводит на экран.

# Пример:
# Введите число: 1234
# Число наоборот: 4321
# 
# Введите число: 1000
# Число наоборот: 0001
# 
# Введите число: 0
# Программа завершена!
# 
# Дополнительно: добейтесь такого вывода чисел, если в его начале идут нули.
# 
# Введите число: 1230
# Число наоборот: 321
# 
# Кстати, нули, которые мы убрали, называются ведущими.
def print_number(number):
    print(number,end='')
def backward_number(number):
    current_number = 0
    while True:
        part_number = number//10
        current_number = number - (part_number *10)
        print_number(current_number)
        number = part_number
        if number == 0:
            break
start_number = int(input("Введите число: "))
print("Число наоборот: ",end='')
backward_number(start_number)

