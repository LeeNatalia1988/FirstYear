# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# print('Введите число N: ')

# n = int(input())
# fact = 1
# if n < 0:
#     print('Вы ввели отрицательное число. Введите неотрицательное: ')
#     n = input()
#     while n > 1:
#         fact = fact*n
#         n = n - 1
# else:
#     while n > 1:
#         fact = fact*n
#         n = n - 1
# print(f'Факториал заданного числа: {fact}')
# Проверка на == 0 не обязательна, так как факт и так == 1

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = int(input("Введите натуральное числа больше 1 - "))

# status = True

# num1 = 0
# num2 = 1
# i = 2

# while status:
#     result = num1 + num2
#     num1 = num2
#     num2 = result
#     i = i + 1

#     if a == result:
#         print(i)
#         status = False
    
#     elif result > a:
#         print(-1)
#         status = False

# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

print('Введите число N: ')

n = int(input())

print('Введите температуру: ')
i = 0
k = 0 #количество дней текущей оттепели
maxk = 0 #количество дней максимальной оттепели
while i <= n:
    a = int(input())
    if a > 0:
        k = k+1
    elif maxk < k:
        maxk = k
        k=0

print(maxk)

# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

min = 0
max = 0
size = 6

init = True

print("Введите 6-ть элементов")
for i in range(size):
    n = int(input())
    if (init):
        min = max = n
        init = False
    if min > n:
        min = n
    if max < n:
        max = n
print(k)








