# Лабороторная работа 7. ОБРАБОТКА ДАННЫХ ИЗ ФАЙЛА. ИСПОЛЬЗОВАНИЕ КОЛЛЕКЦИЙ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

def sex_filtration(employees, sex):
    if sex == "m":
        print(f"Количество женщин: {len(list(filter(lambda x: x[4] == "Male", employees)))}")
    elif sex == "f":
        print(f"Количество женщин: {len(list(filter(lambda x: x[4] == "Female", employees)))}")

def salary_sorting(employees, desc_asc):
    sorted_list = list()

    if desc_asc == "asc":
        sorted_list = list(sorted(employees, key=lambda x: float(x[5].replace('$', ''))))

        print("Сотрудники в порядке возрастания зарплат:")
    elif desc_asc == "desc":
        sorted_list = list(sorted(employees, key=lambda x: float(x[5].replace('$', '')), reverse=True))

        print("Сотрудники в порядке убывания зарплат:")

    for emp in sorted_list[:20]:
        print(f"Имя {emp[1]}, Зарплата ${emp[5]}")

def hasChild(employees, has_or_not):
    if has_or_not == "h":
        print(f"Является родителем: {len(list(filter(lambda x: bool(x[6]), employees)))}")
    elif has_or_not == "n":
        print(f"Не является родителем: {len(list(filter(lambda x: not bool(x[6]), employees)))}")

def lr_10(employees):
    exit = ""
    sex_filter_param = ""
    salary_sorting_param = ""
    has_child_param = ""

    while True:

        if exit.strip() == "n":
            break
        elif exit.strip() != "n" and exit.strip() != "" and exit.strip() != "y":
            input("Для продолжения нажмите \"y\" или \"n\" для завершения")

        print(f"""    1. Отфильтровать по полу;
    2. Сортировать по зарплате;
    3. Отфильтровать на предмет того, является ли сотрудник родителем (h - имеет/n - не имеет)""")
                
        print()

        variant = int(input("Выберите нужный вам вариант: "))

        print()

        if variant == 1:
            sex_filter_param = input("Выберите m (Male) или f (Female): ")

            sex_filtration(employees, sex_filter_param)
        elif variant == 2:
            salary_sorting_param = input("Выберите asc (по возрастанию) или desc (по убыванию)")

            salary_sorting(employees, salary_sorting_param)
        elif variant == 3:
            has_child_param = input("Выберите h (имеет) или n (не имеет)")

            hasChild(employees, has_child_param)

        print()

        y_n = input("Хотите продолжить?(y/n): ")
        exit = y_n

f = open('lr_10\\p7_data_00.csv')
s = f.readlines()
employees = list(map(lambda x: x.strip().split(','), s))
del employees[0]

lr_10(employees)