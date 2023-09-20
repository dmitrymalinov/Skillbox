print('Задача 1. Сумма чисел')

# Напишите функцию summa_n,
# которая принимает одно целое положительное число N 
# и выводит сумму всех чисел от 1 до N включительно.
# 
# Пример работы программы:
# Введите число: 5
# 
# Я знаю, что сумма чисел от 1 до 5 равна 15
def summa_n(number):
    summ_number = 0
    for current_number in range(1,number + 1):
        summ_number += current_number
    print(f"Я знаю, что сумма чисел от 1 до {number} равна {summ_number}")
input_number = int(input("Введите число: "))
summa_n(input_number)