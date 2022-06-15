"""
Реализуйте функцию get_credentials_users(path), которая возвращает список строк из бинарного файла,
созданного в предыдущей задаче, где:

path - путь к файлу.
Формат файла:

andry:uyro18890D
steve:oppjM13LL9e
Откройте файл для чтения, используя with и режим rb. Сформируйте список строк из файла и верните его из
функции get_credentials_users в следующем формате:

['andry:uyro18890D', 'steve:oppjM13LL9e']
Требования:

Используйте менеджер контекста для чтения из файла

"""

def get_credentials_users(path):
    all_in_one = []
    try:
         with open(path, 'rb') as fh:
            for i in fh:
                all_in_one.append(i.decode().strip('\n'))               

    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('The file will be close')
    return all_in_one
    


path_in = ('D:\Code\PY\goit-python\HW_06\AP\Files\\user_pass_10.bin')

print(get_credentials_users(path_in))