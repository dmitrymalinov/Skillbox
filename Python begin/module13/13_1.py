import math
print('Задача 1. Урок информатики 2')


# В прошлый раз учитель написал программу,
# которая выводит числа в формате плавающей точки, однако он вспомнил,
# что не учёл одну важную штуку: числа-то могут идти от нуля.
# 
# Задано положительное число x (x > 0).
# Ваша задача преобразовать его в формат плавающей точки,
# то есть x = a * 10 ** b, где 1 ≤ а < 10
# 
# Обратите внимание, что x теперь больше нуля, а не больше единицы.
# Обеспечьте контроль ввода.
# 
# Пример 1:
# 
# Введитечисло: 92345
# 
# Формат плавающей точки: x = 9.2345 * 10 ** 4
# 
# Пример 2:
# 
# Введите число: 0.0012
# Формат плавающей точки: x = 1.2 * 10 ** -3
# Если у нас число маленькое и степень чилса минусовая то нам надо выйти к 1
#иначе к 0 в делении с остатком
def float_format(number,direction):
    current_number = 0
    while True:
        last_digit = number // math.pow(10,direction)
        ss=1
        if direction < 0:
            if last_digit == 1:
                print(f"Формат плавающей точки: x = {number / math.pow(10,direction)} * 10 ** {direction}")
                break
            direction -= 1
        else:
            if 1 <= last_digit < 10:
                print(f"Формат плавающей точки: x = {number / math.pow(10,direction)} * 10 ** {direction}")
                break   
            direction += 1    
    
number = float(input("Введите число: "))
ss=1
current_direction = number // 10
choose_direction = 0
if current_direction == 0:
    float_format(number,-1)
else:
    float_format(number,1)
