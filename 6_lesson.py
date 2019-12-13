"""
# Загадать случайное число
import random
number = random.randint(1, 100)
#print(number)
user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберите уровень сложности: '))
max_count = levels[level]
user_count = int(input('Введите количество пользователей: '))
users = []
is_winner = False
winner_name = None
for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i+1}: ')
    users.append(user_name)
# Предложить пользователю угадать число
# Сравнить введенное число с загаданным. 
# Создать цикл, чтобы пользователь мог играть пока не угадает
# Добавить количество попыток
while not is_winner:
    count += 1
    if count > max_count:
        print('Попытки закончились. Все пользователи проиграли..')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif  number < user_number:
            print('Ваше число больше загаданного')
        else: 
            print('Ваше число меньше загаданного')
else:
    print(f'{winner_name}, Вы угадали число. Поздравляем!')

import random

min_number = 1
max_number = 100
result = None
while result != '=':
    number = random.randint(min_number, max_number)
    print(number)
    result = input('= > (загаданное число больше вашего) < (загаданное число меньше вашего) ')
    if result == '>':
        min_number = number + 1
    elif result == '<':
        max_number = number - 1
print('Победа!')
"""
#----------------------------------------------------------------------------
# Шаг 1. Загадать случайное число
import random
number = random.randint(1, 100)
#print(number)

# Шаг 2. Предложить пользователю угадать число
user_number = None 
#print(user_number)

# Шаг 3. Сравнить введенное число с загаданным и вывсети результат
# Шаг 4. Добавить цикл до победы пользователя
# Шаг 5. Добавить в игру количество попыток
# Шаг 6. Ограничить количество попыток. 
# Шаг 7. Добавить уровни сложности. Добавить в выбор уровни.
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Введите уровень сложности от 1 до 3: '))
count = 0
max_count = levels[level]
user_count = int(input('Введите количество игроков: '))
users = []
for i in range(user_count):
    user_name = input(f'Введите имя игрока {i+1}: ')
    users.append(user_name)
#print(users)
is_winner = False
name_winner = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Количество попыток закончилось. Все проиграли.')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход игрока {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            name_winner = user
            break
        elif user_number > number:
            print('Ваше число больше загаданного')
        elif user_number < number:
            print('Ваше число меньше загаданного')
else:
    print(f'{name_winner}, Вы угадали число. Поздравляем!')