print('Задача 5. Текстовый редактор')

# Мы продолжаем разрабатывать новый текстовый редактор,
# и в этот раз нам поручили написать для него код,
# который считает количество любой буквы 
# и любой цифры в тексте (а не только буквы Ы как раньше).
# 
# Напишите функцию count_letters,
# которая принимает на вход текст и подсчитывает,
# какое в нём количество цифр K и букв N.
# 
# Функция должна вывести на экран информацию
# о найденных буквах и цифрах в определенном формате.
# 
# Пример:
# Введите текст: 100 лет в обед
# Какую цифру ищем? 0
# Какую букву ищём? л
# 
# Количество цифр 0: 2
# Количество букв л: 1
def count_letters(current_text,number_to_search,letter_to_search):
    count_numbers = 0
    count_letters = 0
    for every_letter in current_text:
        if every_letter == number_to_search:
            count_numbers += 1
        if every_letter == letter_to_search:
            count_letters += 1    
    print(f"Количество цифр {number_to_search}: {count_numbers}")
    print(f"Количество букв {letter_to_search}: {count_letters}")
current_text = input("Введите текст: ")
number_to_search = input("Какую цифру ищем? ")
letter_to_search = input("Какую букву ищем? ")
count_letters(current_text,number_to_search,letter_to_search)