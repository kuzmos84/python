
print("Задание 1")
age = 20
name = "Антон"
weight = 70
print(name, "вес", weight, "кг", "возраст", age, "лет")
age = int(input("Введите Ваш возраст    "))
name = input("Как вас зовут    ")
print("Ваше имя", name, "Ваш возраст", age)

print("Задание 2")
time = int(input("Введите время    "))
hour = time // 3600
min = (time - 3600 * hour) // 60
sec = (time - 3600 * hour) - 60 * min
print(f"{hour:02}:{min:02}:{sec:02}")

print("Задание 3")
n = (input("Введите число    "))
nn = str(n + n)
nnn = str(n + n + n)
print(int(n) + int(nn) + int(nnn))

print("Задание 4")
a = int(input(" ВВедите целое положительное число  "))
b = -1
while a > 0:
    c = a % 10
    a = a // 10
    if c > b:
        b = c
print(b)

print("Задание 5")
revenue = int(input("Введите значение выручки   "))
costs = int(input("ВВедите значение издержек  "))
if revenue > costs:
    print("Фирма получила прибыль")
if revenue < costs:
    print("Фирма получила убыток")
while revenue > costs:
    rentab = revenue / costs
    print("Рентабельность составила", rentab)
    Staff = int(input("ВВедите численность сотружников  "))
    print("Прибыль на одного сотрудника", (revenue - costs) / Staff)
    break

print("Задание 6 ")

days = 1
start = float(input("Введите начальный результат   "))
finish = float(input("ВВедите конечный результат   "))
if start <= 0 or finish <= 0:
    print("ВВедите положительное число  ")
else:
    while start < finish:
        start += start * 0.1
        days += 1
    print("Результат за", days, "дней")
