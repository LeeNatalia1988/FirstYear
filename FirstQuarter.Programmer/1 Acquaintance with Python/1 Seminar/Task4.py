# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый
#  ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, 
# чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

print('Введите общее количество журавликов: ')

S = int(input())

if S%6 != 0:
    print('Вы ввели неверное количество журавликов. Введите верное: ')
    S = int(input())

print(f'Петя сделал {S//6}, Катя сделала {(S//6)*4}, Сережа сделал {S//6}.')