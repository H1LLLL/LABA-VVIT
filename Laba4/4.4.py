import math
import datetime

try:
    a = int(input('Введите число:'))
    print(math.sqrt(a))
except ValueError:
    print("Введите число, а не строку")
print(datetime.datetime.now())
import my_module
try:
    a = int(input('Введите первое число:'))
    b = int(input('Введите второе число:'))
    print(my_module.primer(a, b))
except ValueError:
    print('Вы ввели не числа')
import package_1.m1
import package_1.m2
try:
    print('Введите 2 числа')
    z,x = int(input()),int(input())
    print(package_1.m1.urav_1(z,x))
    print('Введите 2 числа')
    c,d = int(input()),int(input())
    print(package_1.m2.urav_2(c,d))
except ValueError:
    print('Введите числа')