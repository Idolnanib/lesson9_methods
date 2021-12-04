
# написать калькулятор складывающий два числа
# def sum():
#     a = int(input("enter a: "))
#     b = int(input("enter b: "))
#     return a+b
#
# res1 = sum()
# res2 = sum()


# Создать метод, который будет решать уравнение вида 2*x +3 и выводить результат на консоль
def task1():
    x = int(input("Enter x: "))
    print("2 * x + 3 = ",2*x+3)

# y = 6
# task1()


# Написать функцию конвертации рубли в доллары, которая будет возвращать результат конвертации

def convert():
    rub = int(input('Введи количество рублей '))
    doll = int(input('Курс доллара равен : '))
    print(rub * doll)
    return rub+doll

# sum = convert() # сохраним результат конвертации в пекременной sum
# print("sum = ",sum)
# print(sum/2) # поделим на 2



# написать метод деления двух чисел, который возвращает результат деления или None, если знменатель равен нулю
def delit():
    a = int(input('Введи 1 число '))
    b = int(input('Введи 2 число '))
    if b == 0:
        return None
    else:
        return a / b

c = delit()
if c == None:
    print("На аноль делить нельзя")
else:
    print(c)








