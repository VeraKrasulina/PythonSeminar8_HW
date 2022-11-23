# Model

inner_db = {}
# ID REALIZATION
# ID stored in separated File
# get_id (file_name: str) -> next free ID: int
def get_id ():
    with open('id_storage.txt', 'r') as f:
        unique_id = int(f.readline())
    return unique_id


# ID REALIZATION
# ID stored in separated File
# store_id (file_name: str, last used ID: int) -> None
def store_id(unique_id: int):
    with open('id_storage.txt', 'w') as f:
        f.write(str(unique_id))


# Global mapping for database
def global_mapping():
    return {'fist_name' : 'Имя', 'last_name' : 'Фамилия', 'group' : 'Номер класса'}


# 1 CREATE Добавить новую запись
# (input: str -> new data: dict)
# Принемает строку или строки
# Возвращает запись. Запись, принятая от пользователя, новая: {"last_name": last_name, "first_name": first_name, "group": group}
# Уникальный ID добавленный к записи, словарь словарей {number1:{запись1} number2:{запись2}}
def create_new_db_line (user_input: list, mapping: dict):
    global inner_db
    new_id = get_id() + 1
    inner_db[new_id] = {name: value for name, value in zip(mapping.keys(), user_input)}
    store_id(new_id)
    return inner_db


# 2 READ Отобразить запись по ID
# (db: {dict}, id: int -> rec: dict)
# Принимает уникальный ID ввиде цифры
def db_line_print(input_id: int):
    global inner_db
    if input_id in inner_db.keys():
        print(inner_db[input_id].values)
    else:
        print ('Записи с таким ID в базе нет. Попробуйте загрузить базу из файла.')


# 3 UPDATE Обновить запись по ID
# (db: {dict}, ID: int, new data: str -> rec: dict)
def update_db_line (input_id: int, user_input: list, mapping: dict):
    global inner_db
    inner_db[input_id] = {name: value for name, value in zip(mapping.keys(), user_input)}
    print (f'Запись с ID {input_id} обновлена.')
    return inner_db


# 4 DELETE Удалить запись по ID
# (db: {dict}, ID: int -> updated db : {dict})
def delete_line_by_ID (input_id: int):
    global inner_db
    if input_id in inner_db.keys():
        del inner_db[input_id]
        print(f'Запись под номером {input_id} успешно удалена.')
    else:
        print ('Записи с таким ID в базе нет. Попробуйте загрузить базу из файла.')


# 5 export to file (db: {dict}, file_name: str) -> None
# Експорт в файл с сохранением структуры и уникальности ID
def export_to_file (file_name: str):
    global inner_db
    import csv
    column_names = ['ID', 'Имя', 'Фамилия', 'Группа']
    with open (file_name, 'w') as f:
        recorder = csv.DictWriter(f, fieldnames = column_names)
        for person_id, person_info in inner_db.items():
            row = person_info
            row.update({'ID': person_id})
            recorder.writerow(row)
    print(f'Файл {file_name} создан или обновлен.')


# 6 import_with_id (db: {dict}, file_name: str) -> updated db: {dict}
# В файле уже содержатся уникальные ID
def import_from_db_with_id (file_name: str) -> dict:
    import csv
    global inner_db
    column_names = ['ID', 'Имя', 'Фамилия', 'Группа']
    with open (file_name, 'r') as f:
        reciever = csv.DictReader(f, fieldnames = column_names)
        for row in reciever:
            person_info = {}
            for key, value in row.items():
                if not key == 'ID' and value:
                    person_info[key] = value
                inner_db[row['ID']] = person_info
    print(f'Файл {file_name} загружен в память.')
    return inner_db


# 7 import_without_id (db: {dict}, file_name: str) -> updated db: {dict}
# Парсим строку из файла сплитом, получаем список строк?? библиотек, заносим в базу данных, назначая уникальный ID
# (Нужно применять get_id и store_id)

# Парсинг одной из строк файла, который импортируем без ID. Формат строки файла получается должен быть:
# first_name: first_name, last_name: last_name, group: group
def row_parse (file_line: str) -> dict:
    person_info = {}
    info = file_line.split(', ')
    for el in info:
        info = el.split(': ')
        person_info[info[0]] = info[1]
    return person_info


def import_without_id (file_name: str) -> list:
    with open(file_name, 'r') as f:
        file_row = file_name.read().split('\n')
        for el in file_row:
            if el != '':
                inner_db_list = row_parse(el)
    return inner_db_list


def inner_base_from_list_of_dicts(inner_db_list: list) -> dict:
    global inner_db
    i = get_id() + 1
    counter = 0
    while counter < len(inner_db_list):
        inner_db[i] = {i : inner_db_list[counter]}
        counter += 1
        store_id(i)
        i += 1
    return inner_db


# 8 Печать базы данных
def db_printing (db: dict):
    global inner_db
    print('Текущая база данных: \n')
    for p_id, p_info in inner_db.items():
        print('\n"Student ID: "', p_id)
        for key in p_info:
            print(key + ' : ', p_info[key])
