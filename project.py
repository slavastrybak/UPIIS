def compare(num1, num2):
    num1String = str(num1)
    num2String = str(num2)
    num1Count = abs(num1String.find('.') - len(num1String) + 1)
    num2Count = abs(num2String.find('.') - len(num2String) + 1)
    if (num1Count > num2Count):
        print("У числа ", num1, " больше знаков после запятой, чем у ", num2)
    elif(num2Count > num1Count):
        print("У числа ", num2, " больше знаков после запятой, чем у ", num1)
    elif (num1Count == num2Count):
        print("У чисел одинаковое количество знаков после запятой -", num1Count)
    return 0

while (1):
    a = input("Введите первое дробное число с разделителем-точкой: ")
    if (a.isdigit() == True):
        print("Число целое! Повторите ввод.")
    else: break

while (1):
    b = input("Введите второе дробное число с разделителем-точкой: ")
    if (b.isdigit() == True):
        print("Число целое! Повторите ввод.")
    else: break

compare(a, b)