print('Задача 3. Апгрейд калькулятора')

# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. 
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.

# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр, максимальную или минимальную цифру. 

#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.

# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
def sum_digits(number):
    current_sum_digits = 0
    part_number = 0
    while True:
        part_number = number//10
        current_sum_digits += number - (part_number *10)
        number = part_number
        if number == 0:
            break
    print(f"Сумма цифр: {current_sum_digits}")
    calculation()

def max_digit(number):
    part_number = 0
    current_max_number = 0
    current_compare_number = 0
    while True:
        part_number = number//10
        current_compare_number = number - (part_number *10)
        if current_compare_number > current_max_number:
            current_max_number = current_compare_number           
        number = part_number
        if number == 0:
            break        
    print(f"Максимальная цифра: {current_max_number}")
    calculation()
def min_digit(number):
    part_number = 0
    current_max_number = 0
    current_compare_number = 0
    while True:
        part_number = number//10
        current_compare_number = number - (part_number *10)
        if current_max_number == 0:
            current_max_number = current_compare_number
        else:    
            if current_compare_number < current_max_number:
                current_max_number = current_compare_number           
            number = part_number
        if number == 0:
            break        
    print(f"Минимальная цифра: {current_max_number}")
    calculation()

def calculation():
    number = int(input("Введите число: "))
    action = input("Введите одно из действий: сумма цифр, максимальная цифра, минимальная цифра: ")
    if action == "сумма цифр":
        sum_digits(number)
    if action == "максимальная цифра":
        max_digit(number)
    if action == "минимальная цифра":
        min_digit(number)
    else:
        print("Error")
        calculation()
calculation()