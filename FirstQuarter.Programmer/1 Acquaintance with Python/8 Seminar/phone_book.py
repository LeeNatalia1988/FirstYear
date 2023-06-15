
# Задача No(49) 38.
# Решение в группах Создать телефонный справочник с возможностью импорта и
# экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона -
# данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

import os
file = 'phone_book.txt'
fields = ["Фамилия", "Имя", "Отчество", "Телефон", "Описание абонента\n"]
phone_list1 = []
def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1) Вывести справочник на экран\n"
          "2) Сохранить справочник в текстовом файле\n"
          "3) Найти по фамилии\n"
          "4) Найти по имени\n"
          "5) Добавить абонента в текстовый файл\n"
          "6) Удалить абонента из текстового файла")
    choice = int(input())
    return choice

# Ok - основное меню для выбора дальнейшего действия
def work_with_phonebook():
    choice = show_menu()
    while (choice != 7):
        if choice == 1:
            for line in read_from_txt(file):
                print(*line, end='')
            return_to_show_menu()
        elif choice == 2:
            write_to_txt(file, phone_list1)
            print('\nOk', end='')
            return_to_show_menu()
        elif choice == 3:
            finded = input_finded('Введите фамилию:')
            find_abonent(file, finded)
            return_to_show_menu()              
        elif choice == 4:
            finded = input_finded('Введите имя:')
            find_abonent(file, finded)
            return_to_show_menu()
        elif choice == 5:
            add_to_txt(file)
            print('\nOk', end='')
            return_to_show_menu()
        elif choice == 6:
            finded = input_finded('Введите фамилию или имя:')
            delete_from_txt(file, finded)
            print('\nOk', end='')
            return_to_show_menu()
        choice = show_menu()

# Ок - функция для возврата к меню выбора
def return_to_show_menu():
    input('\nНажмите любую клавишу для возврата к основному меню.')

# Ок - функция чтения с тхт файла
def read_from_txt(filename):
    phone_list = [fields]
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            phone_list.append(line.split(','))
    return phone_list

# Ок - функция записи в тхт файл
def write_to_txt(filename, phone_dict):
    with open(filename, 'w+', encoding='utf-8') as file:
        for line in phone_dict:
            file.write(",".join(line))

# Ок - функция добавления в тхт файл данных
def add_to_txt(filename, line = []):
    print('Введите необходимые для записи данные:')
    for item in fields:
        line.append(input(f'\n{item.strip()} > ').title())
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f'{",".join(line)}\n')

# Ок - функция удаления из тхт файла данных
def delete_from_txt(filename, find):
    phone_book = read_from_txt(filename)[1:]
    for line in phone_book:
        if find in line:
            print(*line)
            phone_book.remove(line)
    write_to_txt(filename, phone_book)

# Ок - функция ввода данных для поиска
def input_finded(message):
    answer = input(f'\n{message} > ').title()
    print('\n')
    return answer

# Ок - функция для поиска по введенным в input_finded данным
def find_abonent(filename, find):
    phone_list = read_from_txt(filename)
    find_list = []
    for line in phone_list:
        if find in line:
            find_list.append(line)
    if len(find_list) == 0: print('Не найден.')
    else: 
        find_list.insert(0, fields)
        for line in find_list:
            print(*line, end='')
        return find_list