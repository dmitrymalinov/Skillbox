print('Задача 4. Отрезок')

#Напишите программу, 
# которая считывает с клавиатуры три числа a, b и c,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).
number_a = int(input("Введите число a: "))
number_b = int(input("Введите число b: "))
number_c = int(input("Введите число для проверки кратности c: "))
summ_number = 0
count_number = 0

for current_number in range(number_a,number_b):
    if current_number % number_c == 0:
        summ_number += current_number
        count_number +=1
print(f"Средне арифметическое чисел в диапазоне от {number_a} до {number_b} равно: {summ_number/count_number}")