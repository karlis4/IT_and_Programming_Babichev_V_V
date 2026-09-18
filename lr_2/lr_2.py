# Лабороторная работа 2. УПРАВЛЕНИЕ ХОДОМ ВЫПОЛНЕНИЯ ПРОГРАММЫ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

import math

def denom_calc(denom):
    res = 1.0
    for num in range(int(denom) + 1):
        if num != 0:
            res *= float(num)
    return res

def lr_2(repeat_quantity, pow_x, pow_y, denominator):
    i = 0
    res = 0.0
    while i < repeat_quantity:
        res += - (math.sin(pow(X, pow_x)) * math.log10(pow(Y, pow_y)) / denom_calc(denominator)) 
        + (math.log(pow(X, pow_x + 2)) * math.cos(pow(Y, pow_y + 1)) / denom_calc(denominator + 2.0))
        denominator += 4.0
        pow_x += 4
        pow_y += 1
        i += 1
    return res


X = 4.0
Y = 3.0
pow_x = 1
pow_y = 1
denominator = 1.0
A = 0.0

repeat_quantity = input("Введите кол-во повторений: ")

A = lr_2(int(repeat_quantity), pow_x, pow_y, denominator)

print(f"A = {A}")