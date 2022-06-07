input_number = int(input("Введите число для проверки: "))
if input_number > 10 and input_number < 100 or input_number <= -10 and input_number > -100:
    print("Число двухзначное")
else:
    print("Число не двухзначное")