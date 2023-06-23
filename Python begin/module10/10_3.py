print('Задача 3. Рамка')

# Напишите программу,
# которая рисует с помощью символьной графики прямоугольную рамку.
# Для вертикальных линий используйте символ вертикального штриха “|”,
# а для горизонтальных - дефис “-”. Пусть пользователь вводит ширину и высоту рамки.

#  _ _ _ _ _ _ _ _ _
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |                 |
# |_ _ _ _ _ _ _ _ _|
width = int(input("Введите ширину рамки: "))
height = int(input("Введите высоту рамки: "))
for every_row in range(height+1):
    for every_column in range(width+1):
        ss=1
        if every_row == 0 or every_row == height:
            print("-", end = " ")
        elif every_column == 0 or every_column == width:
            print("|", end = " ")
        else:
            print(" ", end = " ")
    print()