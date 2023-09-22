print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел
# нужно перебрать все простые делители чисел и если остаток от деления обоих чисел равен 0
# тогда это наш ответ. еребирать нужно от 1 до самого большего числа
def great_common_divisor(first_number,second_number):
    biggest_number = 0
    if first_number > second_number:
        biggest_number = first_number
    else:
        biggest_number = second_number
    for every_number in range(1,biggest_number+1):
        if (first_number % every_number == 0) and (second_number % every_number ==0) :
            current_gcd = every_number
    print(f"Наибольший общий делитель чисел {first_number} и {second_number} равен {current_gcd}")

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
great_common_divisor(first_number,second_number)