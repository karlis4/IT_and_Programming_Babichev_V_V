# Лабороторная работа 9. ОБЪЕКТНО-ОРИЕНТИРОВАННОЕ ПРОГРАММИРОВАНИЕ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

import math

class Grafic_y_equal_x:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def integral_a_to_b(self):
        print(f"интеграл функции от a до b равен: {self.a ** 2 / 2 - self.b ** 2 / 2}")

    def length(self):
        print(f"Длина отрезка от (a, y(a)) до (b, y(b)): {(self.b - self.a) - math.sqrt(2)}")

a, b = map(int, input("Введите a и b через пробел: ").split())

graf = Grafic_y_equal_x(a, b)

graf.integral_a_to_b()
graf.length()