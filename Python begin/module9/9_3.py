print('Задача 3. Театр')

# В городе планируют построить театр под открытым небом, но для начала нужно оценить, сколько сделать рядов, сидений в них и каким должно быть расстояние между рядами.

# Что нужно сделать

# Напишите программу, которая получает на вход количество рядов, сидений и свободных метров между рядами, а затем выводит примерный макет театра на экран.


# Сцена
# Введите кол-во рядов: 5
# Введите кол-во сидений ряду: 7
# Введите кол-во метров между рядами: 3
#
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======
# ======= *** =======

row_count = int(input("Введите количество рядов: "))
places_in_row = int(input("Введите количество сидений в ряду: "))
space_betwenn_row = int(input("Введите количество метров между рядами: "))


for vurrent_row in range(row_count):
    current_places_row = ""
    for p in range(places_in_row):
        current_places_row += "="
    print(current_places_row, end=" ")
    current_space_between_row = ""
    for i in range(space_betwenn_row):
        current_space_between_row += "*"
    print(current_space_between_row, end=" ")
    current_places_row = ""
    for p in range(places_in_row):
        current_places_row += "="
    print(current_places_row)
