# # ----- > Тернарный оператор
# # is_has_name = False
# # name = 'Max' if is_has_name else 'Leo'
# # print(name)
#
# # слово -> СлОвО
#
# word = 'словосочетание'
# result = []
#
# for i in range(len(word)):
#     let = word[i]
#     letter = let.lower() if i%2 != 0 else let.upper()
#     result.append(letter)
#
# result = ''.join(result)
# print(result)

# ----- > Генератор списков
# (number for number in numbers if number > 0)

# # записать в список только польжительные числа
# numbers = [1, 2, 3, 4, 5, 0, -1, -2, -3]
#
# # классический способ
# result = []
# for number in numbers:
#     if number > 0:
#         result.append(number)
# print(result)
#
# # через функцию filter
# result = filter(lambda number: number > 0, numbers)
# print(list(result))
#
# # через генератор списка
# result = (number for number in numbers if number > 0)
# print(list(result))
#
# pairs = {(1, 'a'), (2, 'b'), (3, 'c')}
# # классический способ
# result = {}
# for pair in pairs:
#     key = pair[0]
#     val = pair[1]
#     result[key] = val
# print(result)

# # через генератор словаря
# result = {pair[0]: pair[1] for pair in pairs}
# print(result)

# 1. Создать список из случайных чисел от 1 до 100
import random
numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# 2. Создать список квадратов чисел
numbers = [1, 2, 3, -4]
numbers = [i**2 for i in numbers]
print(numbers)

# 3. Создать список имен на букву А
names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']
names = [name for name in names if name.startswith('А')]
print(names)



