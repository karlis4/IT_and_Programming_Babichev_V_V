# Лабороторная работа 7. ОБРАБОТКА ДАННЫХ ИЗ ФАЙЛА. ИСПОЛЬЗОВАНИЕ КОЛЛЕКЦИЙ
# Бабичев В.В.
# ИНБ-б-о-26-1
# Вариант 5

def city_from(tickets):
    print(f"Количество билетов с отправлением из Ставрополя = {len(list(filter(lambda x: x[3] == "Stavropol", tickets)))}")

def every_point(tickets):
    cities_dict = dict()

    for ticket in tickets:

        if ticket[3] not in cities_dict:
            cities_dict[ticket[3]] = [1, float(ticket[5].replace('$', ''))]
        else:
            t = cities_dict[ticket[3]]
            t[0] += 1
            t[1] += float(ticket[5].replace('$', ''))

    for city, q in cities_dict.items():
        print(f"Город: {city}, средняя цена билета: {q[1] / q[0]}")

def wm_bought_tickets(tickets):
    wm = dict({"F": 0, "M": 0})

    for t in tickets:
        if t[2] == "F":
            wm[t[2]] += 1
        elif t[2] == "M":
            wm[t[2]] += 1

    print(f"""Кол-во билетов, купленных мужчинами: {wm["M"]}
Кол-во билетов, купленных женщинами: {wm["F"]}
Кол-во билетов, купленных и мужчинами, и женщинами {wm["M"] + wm["F"]}""")

def eq_from_to(tickets):
    eq_from_to_quantity = 0

    for t in tickets:

        if t[3] == t[4]:
            eq_from_to_quantity += 1

    print(f"Кол-во билетов с совпадающими пунктами прибытия и отправки: {eq_from_to_quantity}")

def lr_7(tickets):
    exit = ""

    while True:

        if exit.strip() == "n":
            break
        elif exit.strip() != "n" and exit.strip() != "" and exit.strip() != "y":
            input("Для продолжения нажмите \"y\" или \"n\" для завершения")

        print(f"""    1. Количество билетов с пунктом отправления из Ставрополя;
    2. Средняя цена билета для каждого из четырёх пунктов отправления;
    3. Количество билетов, купленных женщинами и мужчинами;
    4. Количество билетов с одинаковыми пунктами отправления и прибытия""")
                
        print()

        variant = int(input("Выберите нужный вам вариант: "))

        print()

        if variant == 1:
            city_from(tickets)
        elif variant == 2:
            every_point(tickets)
        elif variant == 3:
            wm_bought_tickets(tickets)
        elif variant == 4:
            eq_from_to(tickets)

        print()

        y_n = input("Хотите продолжить?(y/n): ")
        exit = y_n

f = open('lr_7\\p7_data_05.csv')
s = f.readlines()
tickets = list(map(lambda x: x.strip().split(','), s))
del tickets[0]

lr_7(tickets)