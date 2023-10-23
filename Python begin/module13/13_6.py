import math
print('Задача 6. Яйца')

# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
# 
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
# 
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
# 
# Известно, что глубина точно больше нуля и меньше четырёх метров.
# 
# Обеспечьте контроль ввода.
# 
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
# 
# Приблизительная глубина безопасной кладки: 0.732421875 м
MIN_DEEP = 0
MAX_DEEP = 4

def danger_level(deep_meters):
    current_danger_level = math.pow(deep_meters,3) - 3*math.pow(deep_meters,2) - 12*deep_meters + 10
    return current_danger_level
max_danger_level = float(input("Введите максимально допустимый уровень опасности: "))
#идем от 4 не доходя до 0 на каждой итерации уменьшая глубину в половину
previuous_deep = 0
current_deep = MAX_DEEP
left = 0
rigth = 0
flag = 0
while True:
    current_danger_lvl = danger_level(current_deep)
    if round(current_danger_lvl,2) == max_danger_level:# наш ответ
        print(f"Приблизительная глубина безопасной кладки: {right} м")
        break
    if round(current_danger_lvl,2) > max_danger_level: # перелет
        if flag == 1:
            left = current_deep
            current_deep = (left + right)/2
            continue
        flag = 1
        left = current_deep
        right = previuous_deep
        previuous_deep = current_deep
        current_deep = (left + right)/2
        
        continue
    if round(current_danger_lvl,2) < max_danger_level: # недолет
        if flag == 1:
            right = current_deep
            current_deep = (left + right)/2
            continue
        previuous_deep = current_deep
        current_deep /=2
