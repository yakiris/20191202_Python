task = int(input('Запустить задачу номер: '))
if task == 1:
# 1: Запросите от пользователя число, сохраните в переменную, прибавьте к числу 2 и выведите результат на экран.
# Если возникла ошибка, прочитайте ее, вспомните урок и постарайтесь устранить ошибку.

    num = float(input('Введите число: '))
    print(f'Ваше число плюс 2 = {num + 2}')

if task == 2:
# 2: Используя цикл, запрашивайте у пользователя число, пока оно не станет больше 0, но меньше или равно 10.
# После того, как пользователь введет корректное число, возведите его в степень 2 и выведите на экран.
# Например, пользователь вводит число 123, вы сообщаете ему, что число неверное, и говорите о диапазоне допустимых. И просите ввести заново.
# Допустим, пользователь ввел 2, оно подходит. Возводим его в степень 2 и выводим 4.

    while True:
        num = int(input('Введите целое число от 0 до 10: '))
        if num > 0 and num <= 10:
            print(f'Ваше число возведённое в квадрат = {num**2}')
            break
        else:
            print('Вы ввели неверное число...')

if task == 3:
# 3: Создайте программу “Медицинская анкета”, где вы запросите у пользователя следующие данные: имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии.
#
# (Формула не соответствует реальной действительности и здесь используется только ради примера)
# Примечание: при написание программы обратите внимание на условия в задаче и в вашем коде.  Протестируйте программу несколько раз и убедитесь, что проверки срабатывают верно. В случае ошибок, уточните условия для той или иной ситуации.
# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

    name, surname, old, weight = input('Введите через пробел: имя, фамилию, возраст, вес: ').split()
    if int(old) < 30 and 120 > int(weight) > 50:
        print(f'{name} {surname}, {old} год, вес {weight} - отличное состояние')
    elif int(old) > 30 and 50 > int(weight) > 120:
        print(f'{name} {surname}, {old} год, вес {weight} - следует заняться собой')
    elif int(old) > 40 and 50 > int(weight) > 120:
        print(f'{name} {surname}, {old} год, вес {weight} - следует обратится к врачу!')
    else:
        print(f'{name} {surname} - радуйтесь жизни у вас хорошее состояние!')

# test pull requests