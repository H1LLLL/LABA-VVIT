try:
    a = int(input('Введите число:'))
    if a>=1:
        for i in range(a):
            print(i+1)
    else:
        print('Введите положительное число')
except ValueError:
    print('Введите число, а не символы')
try:
    print('Введите два целых числа:')
    x = int(input())
    y = int(input())
    if x>y:
        print(x)
    elif x<y:
        print(y)
    else:
        print('Числа равны')
except ValueError:
    print('Введите два числа')
