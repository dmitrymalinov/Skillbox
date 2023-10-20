print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример: 

# Введите первое число: 102
# Введите второе число: 123
 
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225
def backward_number(number):
    current_number = 0
    while number > 0:
        last_digit = number % 10
        number = number//10
        current_number = current_number * 10
        current_number = current_number + last_digit
    return current_number

first_number = int(input("Введит первое число: ")) 
second_number = int(input("Введит второе число: ")) 

backward_first_number = backward_number(first_number)
backward_second_number = backward_number(second_number)

print(f"Первое число наоборот: {backward_first_number}")
print(f"Второе число наоборот: {backward_second_number}")
print(f"Сумма: {first_number + second_number}")
print(f"Сумма наоборот: {backward_first_number + backward_second_number}")