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

'''
1. Что такое переменная?

Переменная - это именованная область памяти для хранения данных.

2. Какие имена переменных недопустимы?

99bottles - начинается с цифры
r&d - содержит символ &

3. Sales и sales - одинаковые?

Нет, Python чувствителен к регистру, это разные переменные.

4. Допустима ли инструкция 72 = amount?

Нет, слева должно быть имя переменной, а не число.

5. Что покажет код?
val = 99
print('Значение равняется', 'val')

Выведет: Значение равняется val 

6. Типы данных:

value1 = 99 → int
value2 = 45.9 → float
value3 = 7.0 → float
value4 = 7 → int
value5 = 'abc' → str

7. Что покажет код?
my_value = 99
my_value = 0
print(my_value)

Выведет: 0

8. Перепишите с range():

for x in range(6):
    print('Обожаю эту программу!')

9. Что покажет код?

for number in range(6):
    print(number)

Выведет: 0 1 2 3 4 5

10. Что покажет код?
for number in range(2, 6):
    print(number)

Выведет: 2 3 4 5

11. Что покажет код?
for number in range(0, 501, 100):
    print(number)

Выведет: 0 100 200 300 400 500

12. Что покажет код?
for number in range(10, 5, -1):
    print(number

Выведет: 10 9 8 7 6

13. Что такое накопитель?

Переменная, которая накапливает сумму или результат в цикле.

14. Следует ли инициализировать накопитель?

Да, иначе будет ошибка.

15. Что покажет код?
total = 0
for count in range(1, 6):
    total = total + count
print(total)

Выведет: 15

16. Что покажет код?
number1 = 10
number2 = 5
number1 = number1 + number2
print(number1, number2)

Выведет: 15 5

17. Расширенные операторы:

quantity += 1
days_left -= 5
price *= 10
price /= 2

18. Ввод фамилии:

last_name = input("Введите фамилию клиента: ")

19. Ввод объема продаж:

sales = float(input("Введите объем продаж за неделю: "))

20. Что такое бесконечный цикл?

Цикл, который выполняется бесконечно:

while True:
    print("Бесконечный цикл")
'''