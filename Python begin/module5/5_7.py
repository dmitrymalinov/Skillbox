print('Задача 7. Костя хочет выигрывать')

# После игры в кубики Костя захотел немного изучить работу игровых автоматов,
# а заодно математику и теорию вероятностей.
# Но ему нужно с чего-то начать:
# написать программу, которая поможет выявить закономерности в комбинациях чисел на автомате.
 
# Даны три целых числа.
# Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел:
# 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны).
first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

if first_number == second_number == third_number:
    print(3)
elif (first_number == second_number != third_number) or (first_number == third_number != second_number) or (second_number == third_number != first_number):
    print(2)
else:
    print(0)