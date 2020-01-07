# 3. Напишите функцию которая принимает на вход список. Функция создает из этого списка новый
# список из квадратных корней чисел (если число положительное) и самих чисел (если число отрицательное)
# и возвращает результат (желательно применить генератор и тернарный оператор при необходимости).
# В результате работы функции исходный список не должен измениться.
# Например:
# old_list = [1, -3, 4]
# result = [1, -3, 2]
#
# Примечание: Список с целыми числами создайте вручную в начале файла.
# Не забудьте включить туда отрицательные числа. 10-20 чисел в списке вполне достаточно.

import math
numbers = [1, 2, 3, 8, 15, 16, -8, 4, 18, 24, -6]

# def get_list(numbers):
#     result = []
#     for number in numbers:
#         if number > 0:
#             num = number**2
#         else:
#             num = number
#         result.append(num)
#     return result

def get_list(numbers):
    result = [round(math.sqrt(number), 1) if number > 0 else number for number in numbers]
    return result

result = get_list(numbers)
print(result)
print(numbers)