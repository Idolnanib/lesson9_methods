
# написать метод деления двух чисел, который возвращает результат деления или None, если знменатель равен нулю
# метод должен иметь два параметра, через которые передаются числа
import random


def delit(a,b):
    z = 5
    if b == 0:
        return None
    else:
        return a / b


a = random.randint(2,10)
b = int(input('Введи 2 число '))
c = delit(a,b)
if c == None:
    print("На аноль делить нельзя")
else:
    print(c)
