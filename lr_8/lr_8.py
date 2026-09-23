# Лабороторная работа 8. ПРИМЕНЕНИЕ БИБЛИОТЕЧНЫХ МОДУЛЕЙ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

import builtins

def lr_8(nums):
    nums_amount = 0

    for num in nums:
        oven_sum = 0
        odd_sum = 0
        oct_num = builtins.oct(num)[2:]

        if len(oct_num) != 6:
            continue

        for oct in oct_num:
            if int(oct) % 2 == 0:
                oven_sum += int(oct)
            else:
                odd_sum += int(oct)

        if oven_sum < odd_sum and oct_num == oct_num[::-1]:
            nums_amount += 1

    return nums_amount


f = open('lr_8\\pr8.txt')
s = f.readlines()
nums_arr = list(map(lambda num: int(num.strip()), s))

nums_amount = lr_8(nums_arr)

print(f"Кол-во чисел составляет: {nums_amount}")