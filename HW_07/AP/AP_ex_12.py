"""
Реализуйте функцию file_operations(path, additional_info, start_pos, count_chars), 
которая добавляет дополнительную информацию в файл по пути path из параметра additional_info,
и после этого возвращает строку с позиции start_pos длиной count_chars.

Требования:

функция должна открывать файл с помощью with по пути path в режиме добавления информации
записывать в конец файла строку additional_info
после записи функция должна открыть тот же файл для чтения
прочитать и вернуть строку с позиции start_pos длиной count_chars с помощью функции seek.
Важно: для прохождения задачи необходимо использовать менеджер контекста with, методы seek, write и read
"""

def file_operations(path, additional_info, start_pos, count_chars):
    #добавляем строку в файл
    additional_info = additional_info + '\n'
    try:
         with open(path, 'a') as fh:
            fh.write(additional_info)               

    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('The file will be close')
            
    #открываем файл для поиска строки
    try:
        with open(path, 'r') as fh:
            fh.seek(start_pos)  
            end_str = fh.read(count_chars)
            
    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('The file will be close')
   
    return end_str


def main():
    path_in = ('D:\Code\PY\goit-python\HW_07\AP\Files\some_file.txt')
    add_info = '!!! some text for test !!!'
    start_p = 23 
    count_ch = 26
    print(file_operations(path_in, add_info, start_p, count_ch))

if __name__ == '__main__':
    main()

"""
    def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as f:  
        f.write(additional_info)  
    with open(path, 'r') as f:  
        f.seek(start_pos)  
        end_str = f.read(count_chars)  
    return end_str"""