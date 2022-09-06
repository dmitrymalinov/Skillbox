print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.
deposit_value = int(input('Введите сумму вклада: '))
percent_value = int(input('Введите ставку процентов '))
deposit_finish = int(input('Введите желаемую сумму '))
years_to_finish = 0
while True:
    deposit_value += deposit_value*(percent_value/100)
    deposit_value = deposit_value//1
    years_to_finish +=1
    if deposit_value >= deposit_finish:
        print(f'Понадобиться лет {years_to_finish}')
        break
