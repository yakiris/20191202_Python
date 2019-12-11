"""
friends = 'Максим Леонид '
print(len(friends))
print(friends.find('Лео'))
print(friends.isdigit())
print(friends.lower())
#print('Привет %a. Тебе %b лет?'%('Ivan', 30))
print('Привет {}. Тебе {} лет?'.format('Ivan', 30))

top5 = 'Первые пять мест на соревнованиях: 1. Иванов 2. Петров 3. Сидоров 4. Орлов 5. Соколов'
start = top5.find('1')
end = top5.find('4')
top3 = top5[start:end]
print('Поздравляем {} с успехом!'.format(top3.upper()))
"""
print('соревноване по python'.upper())
count  = int(input('Введите количество участников соревнования: '))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место? '.format(i))
    members.append(name)
    i-=1
print('В соревновании участвовали:', sorted(members))
members.reverse()
top3 = members[:3]
print('Победители {}. Поздравляем!'.format(top3))