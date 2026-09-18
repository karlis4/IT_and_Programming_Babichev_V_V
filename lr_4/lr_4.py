# Лабороторная работа 4. ФАЙЛЫ И ИСКЛЮЧЕНИЯ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

def find_substring(s: str):
    i = 0
    const_str = ""
    tmp_str = ""
    digit_flag = 0

    while i < len(s):
        if s[i].isdigit():
            digit_flag = 1
            tmp_str = ""
            i += 1
        elif digit_flag == 1 and not s[i].isupper():
            i += 1
            continue
        elif s[i].isupper():
            digit_flag = 0
            
            if len(tmp_str) % 3 == 0 and len(tmp_str) > len(const_str):
                const_str = tmp_str
                tmp_str = ""
            else: 
                tmp_str = ""
            i += 1
        else:
            tmp_str += s[i]
            i += 1
        

    return const_str

f = open('lr_4\\data_v1.txt')
s = f.read().strip()

res = find_substring(s)

print(f"Последовательность: {res}, длина: {len(res)}") 