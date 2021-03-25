task = int(input('Запустить задачу номер: '))
if task == 1:
# 1: Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую
# директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки.
# Проверьте работу функций в этом же модуле.
    import os

    def create_folders():
        for i in range(1, 10):
            folder_name = f'dir_{i}'
            os.mkdir(folder_name)

    def delete_folder():
        for i in range(1, 10):
            folder_name = f'dir_{i}'
            os.rmdir(folder_name)

    if __name__ == '__maim__':
        create_folders()
        delete_folder()

elif task == 2:
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