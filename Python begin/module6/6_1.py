print('Задача 1. Кубы чисел')

# Любителю математики Паше снова стало мало распечатанных табличек,
# включая последнюю со степенями двойки.
# Теперь он хочет взять третью степень чисел от 1 до абсолютно любого!

# Напишите программу,
# которая возводит в третью степень каждое число от 1 до N
# и выводит результат на экран.
BEGIN_Number = 1
last_number = int(input('Введите число до которого считать степень: '))
while BEGIN_Number <= last_number:
    print(f"Третья степень числа {BEGIN_Number} равна {BEGIN_Number**3}")
    BEGIN_Number+=1