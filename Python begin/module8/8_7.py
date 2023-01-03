print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
PRICE_INCREASE_PERCENT = 3
educational_grant = int(input("Введите размер стипендии: "))
expenses = int(input("Введите размер расходов: "))
for every_month in range(1,11,1):
    if every_month ==1:
        summ_support = expenses - educational_grant
    else:
        expenses *= 1 + PRICE_INCREASE_PERCENT/100
        summ_support = expenses - educational_grant
    print(f"За месяц {every_month} понадобиться попросить у родителей {summ_support}")