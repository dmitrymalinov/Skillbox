# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
i = ''
# social links
v = ''
t = ''
tk = ''
#my new variables
age = 0
phone_number = ''
email =''
additional_info = ''
#my new functions
def validate_age(age):
    if age > 0:
         return True
    else:
         return False
def phone_number(user_phone):
    for every_symbol in user_phone:
        if every_symbol == '+' or ('0' <= every_symbol <= '9'):
            phone_number += every_symbol          

def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, i_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19: years_parameter = 'лет'
    elif a_parameter % 10 == 1: years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4: years_parameter = 'года'
    else: years_parameter = 'лет'


    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    if i:
            print('')
            print('Дополнительная информация:')
            print(i_parameter)
    

print('Приложение MyProfile для предпринимателей')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
            break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                user_age = int(input('Введите возраст: '))
                if validate_age(user_age):
                    age = user_age
                else:
                    print('Возраст должен быть положительным')
                user_phone =  input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone_number(user_phone)
                email = input('Введите адрес электронной почты: ')
                additional_info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                v = input('Введите адрес профиля Вконтакте: ')
                t = input('Введите логин Telegram: ')
                tk = input('Введите логин Tiktok: ')
            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, i)

            elif option2 == 2:
                general_info_user(n, a, ph, e, i)

                # print social links
                print('')
                print('Социальные сети и мессенджеры')
                print('Вконтакте:', v)
                print('Telegram: ', t)
                print('Tiktok:   ', tk)
            else:   print('Введите корректный пункт меню')
    else:       print('Введите корректный пункт меню')