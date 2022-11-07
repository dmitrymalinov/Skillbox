print('Задача 9. ...Теперь можно посчитать и свою')

# Пока бухгалтер считала среднюю зарплату сотрудников,
# ей стало интересно, а не зря ли она работает столько времени на одном месте?
# Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# 
# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
start_number = 1
previous_rate = 0
error_flag = 0
for current_number in range(1,11):
    current_rate = int(input(f"Введите число {current_number} :"))
    if current_rate > previous_rate: # числа идут по возрастанию
        previous_rate = current_rate
    else:
        error_flag = 1       
    start_number +=1
if error_flag == 1:
    print("Числа не по порядку!")
else:
    print("Числа по порядку!")