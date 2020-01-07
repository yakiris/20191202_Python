# 1: Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:
my_favourite_group = {
'name': 'Г.М.О.',
'tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016},
           {'name': 'Шапито','year': 2014}]
}
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.
import json
j_group = json.dumps(my_favourite_group)
print(j_group)

with open('group.json', 'w', encoding='utf-8') as f:
    json_group = json.dump(my_favourite_group, f)

with open('group.json', 'r') as f:
    my_group = json.load(f)
print(my_group)

import pickle
p_group = pickle.dumps(my_favourite_group)
print(p_group)

with open('group.pickle', 'wb') as f:
    pickle_group = pickle.dump(my_favourite_group, f)

with open('group.pickle', 'rb') as f:
    my_group = pickle.load(f)
print(my_group)