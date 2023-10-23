import math
print('Задача 2. Функция максимума')

# Юра пишет различные полезные функции для Python,
# чтобы остальным программистам стало проще работать. 
# Он захотел написать функцию, которая будет находить максимум из перечисленных чисел. 
# Функция для нахождения максимума из двух чисел у него уже есть. 
# Юра задумался: может быть, её можно как-то использовать для нахождения максимума уже от трёх чисел?

# Помогите Юре написать программу, которая находит максимум из трёх чисел. 
# Для этого используйте только функцию нахождения максимума из двух чисел.

# По итогу в программе должны быть реализованы две функции:
# 1) maximum_of_two — функция принимает два числа и возвращает одно (наибольшее из двух);
# 2) maximum_of_three — функция принимает три числа и возвращает одно (наибольшее из трёх); 
# при этом она должна использовать для сравнений первую функцию maximum_of_two.

# итак общие правила a,b,c если a > b и a > c то макисмум a,иначе если b > c  то b, иначе c

def max_two_numbers(number1,number2):
    max_number = max(number1,number2)
    return max_number

def max_three_numbers(number1,number2,number3):
    current_max_number = max_two_numbers(number1,number2)
    current_max_number = max_two_numbers(current_max_number,number3)
    return current_max_number
number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
number3 = int(input("Введите третье число: "))
max_number = max_three_numbers(number1,number2,number3)
print(f"Максимум трех чисел {number1},{number2},{number3} равен: {max_number}")