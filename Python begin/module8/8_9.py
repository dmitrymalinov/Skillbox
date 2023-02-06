print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))
# numerator
# denominator
END_NUMERATOR = 63
END_DENOMINATOR = 64
sum_i=1
x = int(input("Введите число Х: "))

it=1
numenator = 1
for i in range(1,END_NUMERATOR+1,sum_i):
    numenator*=x-it
    print(f"{x}-{it}={x-it}")
    if it == END_NUMERATOR:
        break 
    sum_i*=2
    it+=sum_i
denominator = 1
it_denominator = 2
sum_i=1
for i in range(2,END_DENOMINATOR+1,sum_i):
    denominator*=x-it_denominator
    print(f"{x}-{it_denominator}={x-it_denominator}")
    if it_denominator == END_DENOMINATOR:
        break 
    sum_i*=2
    it_denominator+=sum_i
print(f"Значение выражения равно: {numenator/denominator}")