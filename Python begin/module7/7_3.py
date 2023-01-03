print('Задача 3. Посчитай чужую зарплату...')

# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании
# и, чтобы облегчить себе жизнь, обратилась к программисту.
 
# Напишите программу,
# которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев 
# и выводит на экран среднюю зарплату за год.
year_income = 0
month_count = 0
for current_month in range(1,13):
    year_income += int(input(f"Введите зарплату за {current_month} месяц: "))
    month_count +=1
average_income = year_income/month_count
print(f"Средняя зарплата за месяц равна {average_income}")