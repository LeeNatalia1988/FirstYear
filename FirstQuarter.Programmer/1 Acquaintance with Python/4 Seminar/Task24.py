# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и 
# нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды 
# с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

print('Введите количество кустов: ')
n = int(input())
array_1 = [0]*n   #создание массива из заданного количества кустов
summ = 0
max_summ = 0
print('Введите количество ягод на каждом кусте: ')
for i in range(n):
    array_1[i] = int(input())   #ввод количества ягод каждого куста
for i in range(len(array_1)):
    if i+2 <= len(array_1) - 1:   
        summ = array_1[i] + array_1[i+1] + array_1[i+2] #подсчет суммы количества ягод по три куста до последнего куста
    elif i+1 == len(array_1) - 1: 
        summ = array_1[i] + array_1[i+1] + array_1[-i-2] #подсчет суммы количества ягод по три куста от предпоследнего до первого куста
    elif i+2 > len(array_1) - 1:
        summ = array_1[i] + array_1[-i] + array_1[-i+1] #подсчет суммы количества ягод по три куста от последнего до второго куста
    if max_summ < summ:
        max_summ = summ   #поиск максимального количества ягод
print(f'Максимальное число ягод, которое может собрать за один заход собирающий модуль: {max_summ}.') 