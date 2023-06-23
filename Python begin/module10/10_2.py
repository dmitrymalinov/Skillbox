print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
value_input = int(input("Введите число: "))
for every_row in range(value_input + 1):
    for every_column in range(every_row):
        print(every_row,end=' ')
    print()