print('Задача 1. Я стал новым пиратом!')

# Старому капитану нужно пополнить команду, но на корабль попадут только достойные! Он отобрал десять человек. Те, кто крикнет слово «Карамба», попадут на борт.

# Что нужно сделать

# Пользователь вводит десять слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».
KEY_WORD = "Карамба"
WORDS_COUNT = 10

Pirates = 0

for i in range(1,WORDS_COUNT+1):
    current_word = input(f"Кркините слово {i}: ")
    if current_word == KEY_WORD:
        Pirates +=1
print(f"Из введенных слов совпало {Pirates}")

