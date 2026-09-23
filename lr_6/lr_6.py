# Лабороторная работа 6. РАБОТА СО СТРОКАМИ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

def show_needed_symbol(symbols: dict):
    symbol_keys = list(symbols.keys())
    i = 0

    while i < len(symbol_keys):
        if i == 0:
            print(f"| {symbol_keys[i]} |", end=" ")
        elif i % 10 != 0:
            print(f"{symbol_keys[i]} |", end=" ")
        else:
            print()
            print(f"| {symbol_keys[i]} |", end=" ")

        i += 1

def choose_symbol(symbols: dict):
    chosen_symbol = ""
    exit = ""
    symbols_keys = list(symbols.keys())

    while True:

        if exit.strip() == "n":
            break
        elif exit.strip() != "n" and exit.strip() != "" and exit.strip() != "y":
            input("Для продолжения нажмите \"y\" или \"n\" для завершения")

        print()
        chosen_symbol = input("Введите искомый символ, чтобы увидеть общее количество символов между двумя одинаковыми символами: ")

        if chosen_symbol.strip() == "" or chosen_symbol not in symbols_keys:
            input("Символ не обнаружен или введена пустая строка")
            continue

        
        res_sum = 0

        s_arr = symbols.get(chosen_symbol)

        for el in s_arr:
            res_sum += el[2]

        print(f"Для символа {chosen_symbol} сумма составляет {res_sum}", end=" ")
        y_n = input("Хотите продолжить?(y/n): ")
        exit = y_n


def remove_symbol_without_pair(symbols_map: dict):
    for k, v in symbols_map.items():
        symbol_arr_len = len(v) - 1
        last_arr = v[symbol_arr_len]

        if last_arr[1] == None or last_arr[2] == None:
            del v[symbol_arr_len]

    return symbols_map

def lr_6(symbols_map: dict, s: str):
    i = 0

    while i < len(s):

        if s[i] not in symbols_map:
            symbols_map[s[i]] = [[f"{s[i]}[{i}]", None, None]]
        elif s[i] == s[i + 1 < len(s)] and s:
            i += 1
            continue
        elif s[i] in symbols_map:
            symbol_arr: list = symbols_map.get(s[i])
            symbol_arr_len = len(symbol_arr) - 1

            if symbol_arr[symbol_arr_len][1] == None:
                first_index: str = symbol_arr[symbol_arr_len][0]
                num_str_index = int(first_index[first_index.find('[') + 1:- 1])
                symbol_arr[symbol_arr_len][1] = f"{s[i]}[{i}]"
                symbol_arr[symbol_arr_len][2] = i - num_str_index - 1
            else:
                symbol_arr.append([f"{s[i]}[{i}]", None, None])

        i += 1

    return remove_symbol_without_pair(symbols_map)
    

f = open("lr_6\\pr6.txt")
s = f.read().strip()

symbols_map = dict()

symbols = lr_6(symbols_map, s)
show_needed_symbol(symbols)
choose_symbol(symbols)