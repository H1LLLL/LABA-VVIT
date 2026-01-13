try:
    radius = int(input('Задайте радиус круга:'))
    if radius <= 0:
        print('Вы ввели не число')
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def get_radius(self):
            return self.radius
        def set_radius(self,new_radius):
            self.radius = new_radius
except ValueError:
    print('Введите целое,положительное число')











