print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было. 
# 
# Напишите программу, 
# которая получает список оценок - N чисел - и выводит на экран сообщение о том, 
# кого сегодня больше: отличников, хорошистов или троечников.
number_students = int(input(f"Введите количество учеников: "))
students_with3 = 0
students_with4 = 0
students_with5 = 0
for student_number in range(1,number_students+1):
    student_result = int(input(f"Введите оценку ученика номер {student_number} 3,4 или 5: "))
    if student_result == 3:
        students_with3 += 1
    elif student_result == 4:
       students_with4 += 1 
    elif student_result ==5:
        students_with5 += 1
if students_with5 > students_with4 and students_with5 > students_with3:
    print("Сегодня больше отличников ")
elif students_with4 > students_with5 and students_with4 > students_with3:
    print("Сегодня больше хорошистов ")
elif students_with3 > students_with4 and students_with3 > students_with5:
    print("Сегодня больше троечников ")