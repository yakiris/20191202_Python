# #------> Функции
# # abs - модуль числа
# print(abs(-7))
# # min, max - минимальное, максимальное значение
# numbers = [1, 5, 7, 85, 0, 65, 10]
# print(min(numbers))
# print(max(numbers))
# # round - округление числа
# print(round(8.256, 2))
# # sum - сумма элементов последовательности
# print(sum(numbers))
# # enumerate - нумерация последовательности
# winners = ['Max', 'Leo', 'Kate']
# for number, winner in enumerate(winners, 1):
#     print(number, winner)

# numbers = []
# for i in range(3):
#     user_number = int(input('Введите число: '))
#     numbers.append(user_number)
# print(f'Минимальное число = {min(numbers)}')
# print(f'Максимальное число = {max(numbers)}')
# print(f'Сумма всех чисел = {sum(numbers)}')

# def get_sep(a, b):
#     return a * b

# print('Моя первая функция')
# print(get_sep('-', 50))
# print('Красивый разделитель')
# print(get_sep('*', 100))
# sep = get_sep('х', 20)
# text = 'Hello {} Func {}'.format(sep, sep)
# print(text)

# def hello_max():
#     print('Hello', 'Max')
# hello_max()

# def hello(who):
#     print('Hello', who)
# hello('Leo')

# def greeting(say='Hello', *args):
#     print(say, args)

# greeting('Leo', 'Hi')
# greeting('Hi', 'Leo')
# #greeting(who='Leo', say='Hi')
# greeting('Poll', 'Hi')
# greeting( 'Max')
# # args - передача любого количества аргументов(параметров) но порядку
# greeting('Hi', 'Max', 'Leo', 'Kate') #приходит кортеж
# # kwargs - передача любого количества аргументов(параметров) но имени

# def get_person(**kwargs):
#     for k, v in kwargs.items():
#         print(k, v)
# get_person(name = 'Leo', age = 20, has_car = True) # приходит словарь

# def f():
#     print('Hello func f')

# def to(f_param):
#     f_param()

# to(f)

# numbers = [1, 2, 3, 4, 4541, 5546, 5, 6, 7, 8, 58, 16]

# def my_filter(numbers, function):
#     result = []
#     for number in numbers:
#         if function(number) == True:
#             result.append(number)
#     return result

# def is_even(number):
#     return number % 2 == 0
# print(sorted(my_filter(numbers, is_even)))

# def is_not_even(number):
#     return number % 2 != 0
# print(sorted(my_filter(numbers, is_not_even)))

# def big4(number):
#     return number > 4
# print(sorted(my_filter(numbers, big4)))

# # лямбда функция
# print(sorted(my_filter(numbers, lambda number: number > 15)))

# # sorted - сортировка последовательности softed(iterable, *, key = None, reverse = False) 
# #                                             (последовательность, ключ сортировки, порядок сортировки)
# print(sorted(numbers, reverse = True)) #сортировка по убыванию
# citis = [('Moscow', 1000), ('London', 500), ('Paris', 300)]
# # сортировка по алфавиту
# print(sorted(citis))
# # сортировка по параметру
# def by_count(city):
#     return city[1]
# print(sorted(citis, key=by_count, reverse=True))
# print(sorted(citis, key = lambda city: city[1]))

# # filter - фильтрация последовательности 
# # filter(function, iterable) (функция, последовательность)

# # набор имен
# names = ('Max', 'Leo', 'Kate')
# # нужно получить строки больше 3-х символов
# print(list(filter(lambda name: len(name) > 3, names)))

# # map -применение функции к каждому елементу последовательности 
# # map(funtion, iterable)
# numbers = [1, 2, 3, 4, 8]

# # получить список квадратов чисел последовательности 
# print(list(map(lambda x: x**2, numbers)))
# # привести числак строке
# print(list(map(lambda x: str(x), numbers)))

# 1: Создайте функцию, принимающую на вход имя, возраст и город проживания человека. 
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def person_info(name, age, city):
    result = f'{name}, {age} год(а), проживает в городе {city}'
    return result

#print(person_info('Василий', 21, 'Москва'))
#print(person_info('Дмитрий', 25, 'Санкт-Петербург'))

#2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def max_numbers(a, b, c):
    result = max([a, b, c])
    return result

#print(max_numbers(2, 8, 19))

# 3: Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50. 
### Поэкспериментируйте с значениями урона и жизней по желанию. 
# ### Теперь надо создать функцию attack(person1, person2). Примечание: имена аргументов можете указать свои. 
# ### Функция в качестве аргумента будет принимать атакующего и атакуемого. 
# ### В теле функция должна получить параметр damage атакующего и отнять это количество от health атакуемого. 
# Функция должна сама работать со словарями и изменять их значения.

player_name = input('Введите имя игрока: ')
player = {
    'name' : player_name,
    'health' : 100,
    'damage' : 50,
    'armor' : 1.2
}

enemy_name = input('Введите имя врага: ')
enemy = {
    'name' : enemy_name,
    'health' : 50,
    'damage' : 30,
    'armor' : 1
}

def get_damage(damage, armor):
    return damage / armor

def attak(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attak(player, enemy)
print(enemy)

attak(enemy, player)
print(player)

# 4: Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.
# Примечание. Функция номер 2 используется внутри функции номер 1 для вычисления урона и вычитания его из здоровья персонажа. 

