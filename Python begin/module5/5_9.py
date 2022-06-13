print('Задача 9. Прогрессивный налог 2')

# Мы уже писали программу, вычисляющую сумму налога по прогрессивной шкале
# в зависимости от полученного заработка:
# 13% на доход до 10 000, 20% 
# на доход от 10 000 до 50 000, 30% на доход выше 50 000.
 
# Однако во многих странах,
# использующих такую шкалу, эта сумма вычисляется более сложным способом: 
# налоговая ставка 30% на доход выше 50 000 означает,
# что 30% уплачивается не со всей суммы,
# а лишь с той ее части, которая превосходит 50 000.

# Аналогично, ставка 20% на доход от 10 000 до 50 000
# обязывает уплатить 20% лишь с той части суммы,
# которая превосходит 10 000, но не превосходит 50 000.
 
# Так, например,
# с дохода 100 000 придется заплатить такой налог:
# 30% * (100 000 − 50 000) + 20% * (50 000 − 10 000) + 13% * 10 000 = 15 000 + 8 000 + 1 300  = 24 300.

# А с дохода 30 000 — такой:
# 20% * (30 000 − 10 000) + 13% * 10 000 = 4 000 + 1 300 =  5 300.

# Напишите программу,
# которая спрашивает у пользователя его доход
# и высчитывает сумму налога для него по вышеописанным правилам.
FIRST_RANGE_RATE = 10000
FIRST_TAX_RATE = 13
SECOND_RANGE_RATE = 50000
SECOND_TAX_RATE = 20
THIRD_TAX_RATE = 30

rate = int(input("Введите сумму дохода: "))
if rate < FIRST_RANGE_RATE:
    current_tax = rate * (FIRST_TAX_RATE/100)
    print(f"Сумма Вашего налога сотавила: {current_tax}")
elif rate >= FIRST_RANGE_RATE and rate <= SECOND_RANGE_RATE:
    current_tax = (rate-FIRST_RANGE_RATE) * (SECOND_TAX_RATE/100) + 10000 * (FIRST_TAX_RATE/100)
    print(f"Сумма Вашего налога сотавила: {current_tax}")
elif rate > SECOND_RANGE_RATE:
    current_tax = (rate - SECOND_RANGE_RATE) * (THIRD_TAX_RATE/100) + (SECOND_RANGE_RATE-FIRST_RANGE_RATE) * (SECOND_TAX_RATE/100) + FIRST_RANGE_RATE * (FIRST_TAX_RATE/100)
    print(f"Сумма Вашего налога сотавила: {current_tax}")