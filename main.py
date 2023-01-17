# разработать программу в помощь гидромедцентру
# Меню:
# 1 - ввод температуры за неделю в список
# 2 - вывод максимальной температуры
# 3 - вывод минимальной температуры
# 4 - запись в файл
# 5 - число хороших дней
# ...
# Q - выход
from Stats import *
from UI import menu

user_choise = ""
temps = [12, 5, -3, 23, 24, 6]
while user_choise != "Q":
    menu()
    user_choise = input("Выберите действие:")
    if user_choise == "2":
        print(get_max(temps))
    if user_choise == "3":
        print(get_min(temps))
    if user_choise == "5":
        print(get_good_days(temps))
print("До новых встреч!")
