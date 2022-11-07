print('Задача 8. Замечательные числа')

#Напишите программу,
# которая находит и выводит все двузначные числа,
# которые равны утроенному произведению своих цифр.
# К таким относятся, например, 15 и 24.
for every_number in range(10,100):
    print(every_number)
    
    first_digit = every_number // 10
    second_digit = every_number % 10
    if first_digit * second_digit * 3 == every_number:
        print(f"Найдено число: {every_number}")