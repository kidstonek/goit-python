"""
Данные о пользователях лучше хранить в формате бинарных файлов. Поэтому вам необходимо создать функцию, которая будет записывать логин и пароль пользователя в файл.

Реализуйте функцию save_credentials_users(path, users_info), которая сохраняет информацию о пользователях с паролями в бинарном файле.

Где:

path - путь к файлу.
users_info - словарь вида {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}, где ключ — логин (username) пользователя, а значение — его пароль (password).

Требования:

Каждая строка файла должна иметь следующий вид "username:password". Такой формат записи используют при Базовой аутентификации. С ней вы уже встречались, когда получали доступ к конспекту.
Откройте файл для записи и сохраните ключ и значение из словаря users_info в виде отдельной строки "username:password" для каждого элемента словаря users_info

"""

users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}

def save_credentials_users(path, users_info):
    
    try:
         with open(path, 'wb') as fh:
            code_str = ''
            for u_key, u_val in users_info.items():
                code_str = u_key + ':' + u_val + '\n'
                fh.write(code_str.encode())
                

    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('The file will be close')
            #fh.close()  - with само закрыло файл не пропускало по-этому
    ...

path_o = ('D:\Code\PY\goit-python\HW_06\AP\Files\\user_pass_10.bin')

save_credentials_users(path_o, users_info)
