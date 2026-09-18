# Лабороторная работа 5. ОБРАБОТКА ДАННЫХ С ИСПОЛЬЗОВАНИЕМ СПИСКОВ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

def lr_5(avg_num, nums_arr):
    i = 0
    pairs_quantity = 0
    valid_pairs = list()
    while i < len(nums_arr):

        if i == 0 and str(nums_arr[i]).endswith('19'):

            if avg_num > nums_arr[i] + nums_arr[i + 1]:
                valid_pairs.append(nums_arr[i] + nums_arr[i + 1])
                pairs_quantity += 1

        elif i == (len(nums_arr) - 1) and str(nums_arr[i]).endswith('19'):

            if nums_arr[i - 1] + nums_arr[i] < avg_num:
                valid_pairs.append(nums_arr[i - 1] + nums_arr[i])
                pairs_quantity += 1
            
        elif str(nums_arr[i]).endswith('19'):

            if nums_arr[i - 1] + nums_arr[i] < avg_num:
                valid_pairs.append(nums_arr[i - 1] + nums_arr[i])
                pairs_quantity += 1

            if nums_arr[i] + nums_arr[i + 1] < avg_num:
                valid_pairs.append(nums_arr[i] + nums_arr[i + 1])
                pairs_quantity += 1
            
        i += 1

    return f"Количество найденых пар = {pairs_quantity}, Максимальная сумма элементов пары = {sum(valid_pairs)}"

f = open('lr_5\\pr5.txt')
s = f.readlines()
nums_arr = list(map(lambda num: int(num.strip()), s))

avg_num = sum(nums_arr) / 10000

print(lr_5(avg_num, nums_arr))