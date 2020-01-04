# 2: Создайте модуль. В нем создайте функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой функция должна вернуть None. Проверьте работу функций в этом же модуле.
#     Примечание: Список для проверки введите вручную. Или возьмите этот: [1, 2, 3, 4]

import random

def get_random(my_list):
    if my_list:
        result = random.choice(my_list)
        return result

if __name__ == "__main__":
    my_list = [1, 5, 8, 'f', 85]
    print(get_random(my_list))
    print(get_random([]))