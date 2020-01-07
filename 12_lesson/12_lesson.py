# ----- > Функция open
# - открывает файл в указанном режиме
# - f = open('first.txt', 'w')
# - file - имя файла
# - mode - режим
#     - r - чтение
#     - w - запись, если файла нет, то создается новый
#     - х - запись, если файла нет, ошибка
#     - а - дозапись
#     - b - двоичный режим
#     - + - открытие на чтение и запись
# - encoding - кодировка

# открываем файл на запись - если файл не существует, то создается
# f = open('first.txt', 'w')

# открываем файл на чтение - если файл не существует, то ошибка
# f = open('second.txt', 'r')

# открываем файл на чтение - если файл существует, то открывается
# f = open('first.txt', 'r')

# ----- > Запись текста в файл
# write - метод записать строку в файл
# writelines - метод записать список строк в файл
# \n - символ конца строки

# f = open('first.txt', 'w')
#
# f.write('Hello\n')
# f.write('World\n')
#
# f.writelines(['Hello\n', 'Python\n'])

# ----- > Чтение из файла
# read - чтение всего файла
# for line in f: - чтение файла построчно
# readlines - чтение файла в список строк

# f = open('first.txt', 'r')

# print(f.read())
#
# for line in f:
#     print(line.replace('\n', ''))

# print(f.readlines())

# ----- > Закрытие файла
# Закрытие файлов необходимо для более экономного расходования ресурсов
# f.close(), но если произойдет исключительная ситуация, то закрытие не произойдет
# with - конструкция закрывающая файл

# f = open('first.txt', 'r')
# for line in f:
#     print(line.replace('\n', ''))
# f.close()
#
# with open('first.txt', 'r') as f:
#     for line in f:
#         print(line.replace('\n', ''))
# print('end')

# ----- > Типы строк в python
# str - обычные строки
# bytes - строки байт
# bytearray - изменяемая строка

# # тип обычной строки
# s = 'Hello world'
# print(type(s))
#
# # тип байт строки
# sb = b'Hello world'
# print(type(sb))
# print(sb)
#
# # действия со строками байт
# # взятие индекса - sb[0] - выводит не символ, а код символа
# # взятие среза - sb[1:3]
#
# print(s[1])
# print(sb[1])
#
# print(s[1:3])
# print(sb[1:3])
#
# for item in sb:
#     print(item)

# ----- > Основные кодировки
# ascii - американские символы
# latin-1 - европейские символы
# utf-8 - универсальная кодировка для большинства языков
# чем универсальней кодировка, тем больше байт для одного символа

# sb = b'Ad'
# print(sb[0])
# print(sb[1])

# ----- > Перевод строки в байты (кодирование)
# 'Hello world'.encode('utf-8')
# При переводе строки str в байты bytes указываем кодировку
# кодировка должна поддерживать символы нужного нам алфавита
#
# s = 'Hello world'
# sb = s.encode('ascii')
# print(sb)
# print(type(sb))
#
# s = 'Привет Мир'
# sb = s.encode('utf-8')
# print(sb)
# print(type(sb))

# ----- > Перевод байт в строку (декодирование)
# sb.decode('utf-8')
# указать кодировку, которой кодировали строку

# s = sb.decode('utf-8')
# print(s)

# ------ > Работа с файлом в байтовом режиме
# open('filename', 'wb') - режим записи байтов
# open('filename', 'rb') - режим чтения байтов
# параметр encoding опеределяет кодировку

# with open('bytes.txt', 'wb') as f:
#     pass
#
# with open('bytes.txt', 'rb') as f:
#     pass
#
# with open('bytes.txt', 'r', encoding='utf-8') as f:
#     pass
#
# ----- > Запись байтов в файл
# f.write(b'some bytes') - файл открыт в режиме wb
# f.write('some str') - файл открыт в режиме w
# в любом случае информация хранится в виде 0 и 1

# with open('bytes.txt', 'wb') as f:
#     f.write(b'Hello bytes')
#
# with open('bytes.txt', 'r', encoding='ascii') as f:
#     print(f.read())
#
# with open('bytes.txt', 'wb') as f:
#     str = 'Привет мир'
#     f.write(str.encode('utf-8'))
#
# with open('bytes.txt', 'r', encoding='utf-8') as f:
#     print(f.read())

# ----- > Чтение байтов из файла
# f.read() - файл открыт в режиме rb - читаем байты
# f.read() - файл открыт в режиме r - читаем строки

# with open('bytes.txt', 'wb') as f:
#     str = 'Привет мир'
#     f.write(str.encode('utf-8'))
#
# with open('bytes.txt', 'w', encoding='utf-8') as f:
#     #str = 'Привет мир'
#     f.write('Привет мир')
#
# with open('bytes.txt', 'rb') as f:
#     # читаем байты
#     result = f.read()
#     print(result)
#     print(type(result))
#     # декодируем для получения строки
#     s = result.decode('utf-8')
#     print(s)

# ----- > Сериализация
# - это процесс преобразования объектов в поток байтов для сохранения или
# передачи в память, базу данных или файл, передача объекта посети
# - обратный процесс - десериализация
# ----- > Способы записи объекта в файл
# - ручной
# не универсальный
# трудоемкий
# - универсальный модулем pickle
# сохраняет сложные объекты в файл
# преобразовывает сложные объекты в байты
# встроен в python

# ручной способ
# person = {'name': 'Max', 'phones': [123, 841]}
# # откроем файл
# with open('person.dat', 'wb') as f:
#     # например записам объект в файл построчно
#     # сначала возьмем имя
#     name = person['name']
#     # добавим перенос строки, переведем в байты и запишем
#     f.write(f'{name}\n'.encode('utf-8'))
#     # полчим телефоны
#     phones = person['phones']
#     # запишем 1 телефон в новую строку
#     for phone in phones:
#         f.write(f'{phone}\n'.encode('utf-8'))
# print('Объект записан')
#
# pickle. Основные функции
# - dump - сохранение объекта в файл
# - dumbs - преобразование объекта в байты
# - load - загрузка объекта из файла
# - loads - загрузка объекта из набора байт

# import pickle
# #
# # person = {'name': 'Max', 'phones': [123, 841]}
# #
# # # Открываем файл
# # with open('person.dat', 'wb') as f:
# #     # сразу пишем объект целиком с помощью pickle
# #     pickle.dump(person, f)
# # print('Объект записан')
# #
# # with open('person.dat', 'rb') as f:
# #     # сразу пишем объект целиком с помощью pickle
# #     person = pickle.load(f)
# # print(person)

# ----- > Формар Json
# - JavaScript Object Notation
# - текстовый формат обмена данными, основанный на JavaScript
# - аналогичен набору словарей, списков, простых данных в python
# - но является просто текстом (строкой)
# ----- > Применение
# - хранение данных
# - передача данных
# - чаще всего используется в web разработке
# - для передачи данных по протоколу http
# - требуется только преобразование в строку и обратно
# Json. Основные функции
# - dump - сохранение объекта в формате Json в файл
# - dumbs - преобразование объекта в Json (в текст), но не сохраняет
# - load - загрузка объекта из файла
# - loads - загрузка объекта из формата Json (строки)

import json
# преобразование данных
# friends = [
#     {'name': 'Max', 'age': 23, 'phones': ['123', '456']},
#     {'name': 'Leo', 'age': 33}
# ]
# # посмотрим тип объекта
# print(type(friends))
# # преобразуем список в json
# json_friends = json.dumps(friends)
# # печатаем что получилось
# print(json_friends)
# # проверим тип
# print(type(json_friends))
#
# friends = json.loads(json_friends)
# print(friends)
# print(type(friends))

# сохранение даныхв файл
friends = [
    {'name': 'Max', 'age': 23, 'phones': ['123', '456']},
    {'name': 'Leo', 'age': 33}
]
# посмотрим тип объекта
print(type(friends))
# открываем файл
with open('friends.jon', 'w') as f:
    # преобразуем список в json
    json_friends = json.dump(friends, f)

# обратно из файла в объект
with open('friends.jon', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))

