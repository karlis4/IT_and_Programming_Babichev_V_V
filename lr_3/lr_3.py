# Лабороторная работа 3
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

def honest_sum_nums(N):
    i = 1
    sum = 0

    while i <= N:
        if i % 2 == 0:
            sum += i
        i += 1

    return sum

N = int(input("Введите натуральное число: "))

result = honest_sum_nums(N)

print(f"Сумма натуральных чётных чисел: {result}")