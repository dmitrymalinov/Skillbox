print('Задача 4. С заботой о природе')

# Огромный заповедник поделён на большое количество секторов.
# И у каждого сектора есть номер.
# Мы ответственны за группу секторов с номерами с 30-го по 35-ый
# и нам нужно следить за тем, чтобы посетителей в каждом секторе было меньше 10.
# А заодно и фиксировать для общей статистики, сколько раз это правило было нарушено.
# 
# Напишите программу,
# которая для каждого сектора запрашивает текущее количество людей в нём,
# и если оно больше 10, то фиксирует нарушение.
# В конце выведите количество нарушений
# 
# Пример:
# 
# Людей в 30 секторе: 7
# Всё спокойно.
# Людей в 31 секторе: 11
# Нарушение! Слишком много людей в секторе!
# Людей в 32 секторе: 100
# Нарушение! Слишком много людей в секторе!
# Людей в 33 секторе: 10
# Всё спокойно.
# Людей в 34 секторе: 0
# Всё спокойно.
# Людей в 35 секторе: 1
# Всё спокойно.
# Количество нарушений: 2
MAX_PEOPLE_IN_SECTOR = 10
current_errors = 0
for current_sector in range(30,36):
    current_people = int(input(f"Введите число людей в секторе {current_sector}: "))
    print(f"Людей в {current_sector} секторе: {current_people}")
    if current_people > MAX_PEOPLE_IN_SECTOR:
        print("Нарушение! Слишком много людей в секторе!")
        current_errors +=1
    else:
        print("Всё спокойно.")
print(f"Количество нарушений: {current_errors}")
