print('Задача 5. Счастливый билетик')

# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе номер билета из четного количества цифр
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
ticket_number = int(input('Введите номер билета: '))
check_number = ticket_number
# проверим что число содержит четное количество цифр
number_of_digits = 0
while ticket_number:
    number_of_digits +=1
    check_number //=10
    if check_number == 0:
        break

if number_of_digits == 6:# можно продолжать
    first_three_number = ticket_number//1000
    second_three_number = ticket_number - (first_three_number*1000)
    #Сумма первых трех чисел
    first_digit_first_three_number = first_three_number //100
    second_digit_first_three_number = (first_three_number - (first_digit_first_three_number*100))//10
    third_digit_first_three_number = first_three_number - (first_digit_first_three_number*100)-(second_digit_first_three_number*10)
    sum_digits_first_three_number = first_digit_first_three_number + second_digit_first_three_number + third_digit_first_three_number
    #Сумма вторых трех чисел
    first_digit_second_three_number = second_three_number //100
    second_digit_second_three_number = (second_three_number - (first_digit_second_three_number*100))//10
    third_digit_second_three_number = second_three_number - (first_digit_second_three_number*100)-(second_digit_second_three_number*10)
    sum_digits_second_three_number = first_digit_second_three_number + second_digit_second_three_number + third_digit_second_three_number
    #Сравнение
    if sum_digits_first_three_number == sum_digits_second_three_number:
        print('Билетик счастливый')
    else:
        print('Билетик не счастливый')
else:
    print('Число цифр не верное. Номер должен иметь 6 цифр')
