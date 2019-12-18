# math - библиотека (фнкция) содежащая некоторые математические функции, работа с числами
# factorial - факториал
# exp - экспонента
# log, log2, log10 - логарифмы
# sqrt - квадратный корень
# sin, cos, asin, acos... - тригонометрические функции
# from math import pi
# print(pi)

# random - библиотека
# import random
# print(random.randint(1, 10))

# import math
# # найти длину окружности с определенным радиусом
# r = 16
# print(round(2*math.pi*r, 3))
# # найти площадь окружности с определенным радиусом
# print(round(math.pi * (r ** 2), 3)) # возведение в степень средствами python
# print(round(math.pi * pow(r, 2), 3)) # возведение в степень функцией pow из библиотеки math
# # по координатам 2-х точек определить расстояние между ними
# x1 = 10
# y1 = 10
# x2 = 50
# y2 = 100
# l = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
# print(round(l, 3))
# # найти факториал числа 9
# print(math.factorial(9))

# random - генерирует случайные буквы, числа, элементы последовательности
# randint(1, 10) - случайное целое число издиапазона чисел
# choice - случайный элемент последовательности
# shuffle - перемешивает последовательность случайным образом
# random - случайное число от 0 до 1
# sample - случайный список длиной K из последовательности

# from random import randint, choice, sample, shuffle

# # 1. загадать случайное число от 0 до 100
# print(randint(0, 100))

# # 2. выбрать победителя лотереи из списка players
# players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
# print(choice(players))

# # 3. выбрать трех победителей из списка players
# print(sample(players, 3))

# # 4. перемешать карты в стопке cards
# cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
# print(cards)
# shuffle(cards)
# print(cards)

# # свои функции/библиотеки
# import moda
# from folderb.modb import foo, bar
# #import modc
# from modc import foo

# moda.bar()
# print(moda.foo)

# bar()
# print(foo)

# print(foo)

# # if_name_ == '_main_' - Ограничивает выполнение скриптов
# # при импорте код не будет выполняться, но выполняется при запуске самого модуля
тест для пуша

