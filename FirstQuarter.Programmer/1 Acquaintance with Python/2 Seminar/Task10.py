# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

print('Введите количество монеток: ')
n = int(input())

i = 0
reshka = 0
orel = 0

print('Введите варианты (орел - 0, решка - 1): ')
while i < n:
    version = int(input())
    if version == 1:
        reshka = reshka + 1
    else:
        orel = orel + 1
    i=i+1

if reshka > orel:
    print(f'Нужно перевернуть {orel} монет/ы.')
elif reshka == orel:
    print('Без разницы. Одинаковое количество обоих вариантов.')
else:
    print(f'Нужно перевернуть {reshka} монет/ы.')