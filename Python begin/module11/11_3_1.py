import math
import time

file = int(input('Укажите размер файла: '))
speed = int(input('Какова скорость вашего соединения? '))
second = 1
str_info = 'Прошло {0} секунд. Скачено {1} Мб из {2} Мб ( {3}% )'

for mb in range(speed, file, speed):
    print(str_info.format(second, mb, file, math.ceil(100 * mb / file)))
    second += 1
    time.sleep(1)
else:
    print(str_info.format(second, file, file, math.ceil(100 * file / file)))