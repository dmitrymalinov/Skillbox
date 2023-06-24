print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.
numbers_count = int(input("Введите количество чисел: "))
current_simple_number = 0
summ_numbers = 0
number_to_operate = 0
current_summ_numbers = 0
for every_number in range(numbers_count):
    simple_number_to_check = int(input("Введите число: "))
    # число проверяется на простоту по алгоритму перебора делителей. от 2 до числа. Есть вариант с корнем
    # он описан в википедии
    for every_divider in range(2,simple_number_to_check):
        if simple_number_to_check % every_divider == 0:
            break # если у нас попалось число на которое делится введенное число то это уже не простое число
        else:
            ss=1#считаем сумму чисел
            number_to_operate = simple_number_to_check
            while number_to_operate > 0:
                current_digit = number_to_operate % 10
                current_summ_numbers += current_digit
                number_to_operate = number_to_operate // 10
            if current_summ_numbers >  summ_numbers:
                summ_numbers = current_summ_numbers
                current_simple_number = simple_number_to_check
            current_summ_numbers = 0
            break
print(f"Простое число: {current_simple_number}")
print(f"Сумма чисел: {summ_numbers}")