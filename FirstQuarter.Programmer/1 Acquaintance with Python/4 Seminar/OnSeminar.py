# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# stroka = input().split()
# result = {}
# for i in stroka:
#     if i in result:
#         print(f'{i}_{result[i]}', end=' ')
#     else:
#         print(i, end=' ')
#     result[i] = result.get(i, 0) + 1



# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = input().split()
# set_result = set(inputStr.lower().replace(".", " ").split())
# for i in text:
#     set_result.add(i.lower())
# print(len(set_result))

# На вход программе подаются две строки текста, содержащие по одному слову из перечня "камень", "ножницы", "бумага",
# "ящерица" или "Спок". На первой строке записан выбор Тимура, на второй – выбор Руслана.

# Формат выходных данных
# Программа должна вывести результат жеребьёвки: кто победил - Тимур или Руслан, или они сыграли вничью.

# Примечание. Правила игры стандартные: ножницы режут бумагу. Бумага заворачивает камень. 
# Камень давит ящерицу, а ящерица травит Спока, в то время как Спок ломает ножницы, которые, в свою очередь, 
# отрезают голову ящерице, которая ест бумагу, на которой улики против Спока. Спок испаряет камень, а камень, 
# разумеется, затупляет ножницы.


a = input()
b = input()
key = a +'-'+ b
m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
        'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
        'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
        'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
        'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
        'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
        'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
        'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
        'Спок-ящерица': 'Руслан'}
print(f'Победил: {m[key]}')

