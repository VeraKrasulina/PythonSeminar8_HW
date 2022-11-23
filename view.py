# view
# Предложить юзеру меню:
# 1 CREATE
# 2 READ
# 3 UPDATE
# 4 DELETE
# 5 EXPORT
# 6 IMPORT1 (with ID)
# 7 IMPORT (without ID)
# 8 EXIT

def main_menu ():
    print('\n'
        'Для работы с базой данных, выберите опцию: \n'
        "1 - Добавить новую запись в базу данных.\n"
        "2 - Найти запись в базе данных по ID записи.\n"
        "3 - Обновить запись в базе данных.\n"
        "4 - Удалить запись из базы данных.\n"
        "5 - Сохранить базу данных в файл.\n"
        "6 - Загрузить базу данных в программу.\n"
        "7 - Загрузить данные без ID в программу.\n"
        "8 - Показать базу данных.\n"
        "9 - Прервать работу с программой (не забудьте сохранить данные).\n"
        "Введите ваш выбор: ")
    return input()


def custom_input_rec () -> list:
    fst_name = input("Введите Имя: ")
    lst_name = input("Введите фамилию: ")
    class_name = input("Введите номер класса/группы: ")
    return [fst_name, lst_name, class_name]


def id_for_input () -> int:
    change_id = int(input('Введите необходимый ID: '))
    return change_id


def file_name () -> str:
    file_name = input("Введите название файла бызы данных: ")
    return file_name