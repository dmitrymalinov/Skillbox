# MyProfile app
SEPARATOR = '------------------------------------------'
# user profile
name = ''
age = 0
phone_number = ''
email = ''
zip_code = ''
address = ''
additional_info = ''
# entrepreneur_info
ogrn_ip = ''
inn = ''
bank_account = ''
bank_name = ''
bank_id = ''
corr_bank_account = ''
# functions


def validate_age(age):
    if age > 0:
        return True
    else:
        return False


def phone_number(user_phone):
    current_phone_number = ''
    for every_symbol in user_phone:
        if every_symbol == '+' or ('0' <= every_symbol <= '9'):
            current_phone_number += every_symbol
    return current_phone_number


def input_length_check(user_input, Length):
    current_length = 0
    for every_symbol in user_input:
        if '0' <= every_symbol <= '9':
            current_length += 1
    if current_length == Length:
        return True
    else:
        return False


def zip_code_only_digit(zip_code_user_input):
    current_zip_code = ""
    for every_symbol in zip_code_user_input:
        if '0' <= every_symbol <= '9':
            current_zip_code += every_symbol
    return current_zip_code           
    

def general_info_user(name, age, phone_number, email, zip_code, address, additional_info):
    print(SEPARATOR)
    print('Имя:    ', name)
    if 11 <= age % 100 <= 19:
        years_parameter = 'лет'
    elif age % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'


    print('Возраст:', age, years_parameter)
    print('Телефон:', phone_number)
    print('E-mail: ', email)
    print('Индекс: ', zip_code)
    print('Адрес: ', address)
    if additional_info:
        print('')
        print('Дополнительная информация:')
        print(additional_info)


def entrepreneur_info(ogrn_ip, inn, bank_account, bank_name, bank_id, corr_bank_account):
    print('')
    print("Информация о предпринимателе")
    print(f"ОГРНИП: {ogrn_ip}")
    print(f"ИНН: {inn}")
    print(f"Р/с: {bank_account}")
    print("Банковские реквизиты")
    print(f"Банк: {bank_name}")
    print(f"БИК: {bank_id}")
    print(f"К/с: {corr_bank_account}")


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
                name = input('Введите имя: ')
                while True:
                    user_age = int(input('Введите возраст: '))
                    if validate_age(user_age):
                        age = user_age
                        break
                    else:
                        print('Возраст должен быть положительным')
                user_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone_number = phone_number(user_phone)
                email = input('Введите адрес электронной почты: ')
                zip_code_user_input = input("Введите почтовый индекс: ")
                zip_code = zip_code_only_digit(zip_code_user_input)
                address = input("Введите почтовый адрес (без индекса): ")
                additional_info = input('Введите дополнительную информацию:\n')
            elif option2 == 2:
                # input entrepreneur info 
                while True:
                    ogrn_ip_user_input = input("Введите ОГРНИП: ")
                    if input_length_check(ogrn_ip_user_input, 15):
                        ogrn_ip = ogrn_ip_user_input
                        break
                    else:
                        print("ОГРНИП должен содержать 15 цифр")
                inn_ip_user_input = input("Введите ИНН: ")
                while True:
                    bank_account_user_input = input("Введите расчетный счет: ")
                    if input_length_check(bank_account_user_input, 20):
                        bank_account = bank_account_user_input
                        break
                    else:
                        print("Расчетный счет должен содержать 20 цифр")
                bank_name = input("Введите название банка: ")
                bank_id = input("Введите БИК: ")
                corr_bank_account = input("Введите корреспондентский счет: ")
            else:
                print('Введите корректный пункт меню')
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
                general_info_user(name, age, phone_number, email, zip_code, address, additional_info)

            elif option2 == 2:
                general_info_user(name, age, phone_number, email, zip_code, address, additional_info)

                entrepreneur_info(ogrn_ip, inn, bank_account, bank_name, bank_id, corr_bank_account)
            else:
                print('Введите корректный пункт меню')
    else:
        print('Введите корректный пункт меню')
