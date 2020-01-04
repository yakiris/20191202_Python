# 3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций.
# Вызовите каждую функцию в main.py и проверьте что все работает как надо.
# Примечание: Попробуйте импортировать как весь модуль целиком (например из задачи 1), так и отдельные функции из модуля.

import practice10_2
from practice10_1 import create_folders, delete_folder

create_folders()
delete_folder()
print(practice10_2.get_random([1, 2, 9, 105]))
print(practice10_2.get_random([]))

