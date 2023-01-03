print('Задача 9. Игра «Угадай число»')

# В одном из домашних заданий мы делали задачу, 
# где папа-программист написал для сына программу, которая просит его угадать число.
# Недостаток программы был в том, 
# что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. 
# Теперь, когда мы знаем гораздо больше,
# пришло время исправить этот недостаток и заодно немного улучшить саму игру.
 
# Напишите программу-игру,
# которая запрашивает у пользователя число до тех пор,
# пока он его не отгадает.
# Выводите сообщения в соответствии с примером.
 
# Пример (загадали число 7):
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4
num_try = 0
num_target = int(input('Загадайте число: '))
while True:
    num_input = int(input('Введите число: '))
    num_try +=1
    if num_input > num_target:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    if num_input < num_target:
       print('Число меньше, чем нужно. Попробуйте ещё раз!') 
    if num_input == num_target:
        print(f'Вы угадали! Число попыток: {num_try}')
        break