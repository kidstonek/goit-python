"""
Есть файл со списком сотрудников компании. В каждой строке файла записана информация только про одного сотрудника.
Формат записи, в учебных целях, упрощенный в виде имени сотрудника, символа пробела и его должности, т.е. кем он работает.

John courier
Pipe cook
Создайте функцию get_employees_by_profession(path, profession). 
Функция должна в файле (параметр path) найти всех сотрудников указанной профессии (параметр profession)

Требования:

откройте файл при помощи with для чтения.
получите строки из файла при помощи метода readlines()
с помощью метода find найдите все строки в файле, где есть указанная profession, и поместите записи в список.
объедините все эти строки в списке в одну строку при помощи метода join (помните про перевод строк '\n' и лишние пробелы,
которые надо убрать).
уберите значение 'profession' (замените на пустую строку "" при помощи метода replace).
верните итоговую строку из файла


"""
def get_employees_by_profession(path, profession):
    #открываем файл для поиска строки
    result_string = ''
    result_list = []
    try:
        #читаем файл и ищем вхождение
        with open(path, 'r') as fh:
            while True:
                line = fh.readline()
                if profession in line:
                    result_list.append(line)
                #print(line)
                if not line:
                    break
                    
            
    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('The file will be close')

            for i in result_list:
               result_string = result_string + i
   
    return result_string.replace("\n", '').replace(profession, '').rstrip()
    #result_string.replace(profession,'')




def main():
    path_in = ('D:\Code\PY\goit-python\HW_07\AP\Files\some_text.txt')
    info_pro = 'boss'
    print(get_employees_by_profession(path_in, info_pro))

if __name__ == '__main__':
    main()