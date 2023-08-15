import math
print('Задача 2. Грубая математика')

# В одном аналитическом центре,
# где занимаются разного рода математическим анализом,
# работал практикант,
# который написал программу для расчёта некоторых функций.
# Правда, он в тот день очень устал
# и немного не так прочитал техническое задание 
# и функции теперь рассчитываются довольно грубо.
# 
# Вводится последовательность из N вещественных чисел.
# При этом положительные числа округляются вверх, отрицательные округляются вниз.
# 
# Напишите программу,
# которая выводит натуральный логарифм от числа,
# если оно положительное, и экспоненту в степени числа, если оно отрицательное или равно нулю.
# 
# Пример:
# 
# Введите кол-во чисел: 3
# Введите число: 1.3
# x = 2   log(x) = 0.6931471805599453
# 
# Введите число: -2.1
# x = -3   exp(x) = 0.049787068367863944
# 
# Введите число: -5.9
# x = -6   exp(x) = 0.0024787521766663585
numbers_count = int(input("Введите количество чисел: "))
for every_number in range(1,numbers_count+1):
    current_real_number = float(input(f"Введите число {every_number}: "))
    if current_real_number > 0 :
        number_to_calculate = math.ceil(current_real_number)
        log_current_real_number = math.log(number_to_calculate)
        print(f"x = {number_to_calculate}   log(x) = {log_current_real_number}")
    elif current_real_number < 0 :
        number_to_calculate = math.floor(current_real_number)
        exp_current_real_number = math.exp(number_to_calculate)
        print(f"x = {number_to_calculate}   exp(x) = {exp_current_real_number}")
