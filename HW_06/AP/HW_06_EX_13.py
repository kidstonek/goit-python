"""
Реализуйте функцию create_archive(path, file_name, employee_residence)

Где:

path — путь к файлу
file_name — имя файла
employee_residence — словарь, в котором ключ — имя пользователя, а его значение — страна проживания. Вид: {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}
Функция должна работать следующим образом:

Создавать бинарный файл file_name по пути path
Сохранять данные словаря employee_residence в файл, где каждая новая строка — это ключ значение через пробел как 'Michael Canada'
Архивировать папку по пути path с помощью shutil
Имя архива должно быть 'backup_folder.zip'
Функция должна вернуть строку пути к архиву 'backup_folder.zip'

Требования:

запишите содержимое словаря employee_residence в бинарный файл с именем file_name в папке path с помощью оператора with.
используйте символ /, чтобы разделить путь для path и file_name
вид строки файла — Michael Canada, в конце каждой строки добавляется перевод строки '\n'.
при сохранении строка файла кодируется методом ecnode
при записи строк используем только метод write
архив должен быть в формате zip с именем 'backup_folder' созданный при помощи make_archive.

"""

import shutil


def create_backup(path, file_name, employee_residence):
    
    try:
        with open(path + '/' + file_name, 'wb') as fh:
            code_str = ''
            for u_key, u_val in employee_residence.items():
                code_str = u_key + ' ' + u_val + '\n'
                fh.write(code_str.encode())
                
        shutil.make_archive('backup_folder', 'zip', path)
                

    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('The file will be close')
    
    return path + '/' + 'backup_folder' + '.' + 'zip'

"""for shortcut, description in shutil.get_archive_formats():   <---- просто вівод что может пакет shutil
    print('{:<10} | {:<10}'.format(shortcut, description))"""

employee_residence_in = {'Michael': 'Canada', 'John':'USA', 'Liza': 'Australia'}

path_o = ('D:\Code\PY\goit-python\HW_06\AP\Files')

file_name_in = 'filename'

print(create_backup(path_o, file_name_in, employee_residence_in))