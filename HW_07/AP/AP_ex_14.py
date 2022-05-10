"""
Напишите функцию to_indexed(start_file, end_file), которая будет считывать содержимое файла,
добавлять к считанным строкам порядковый номер и сохранять их в таком виде в новом файле.

Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела,
после чего должен идти текст строки из исходного файла. Нумерация строк идет от 0.
"""
def to_indexed(start_file, end_file):
    try:
        #читаем файл
        temp_list = [] 
        counter = 0
        with open(start_file, 'r') as fh:
            while True:
                line = fh.readline()
                temp_list.append(str(counter) + ": " + line)
                counter += 1        
                if not line:
                    break
        # записіваем в файл
        with open(end_file, 'w') as write_to_file:
            for i in temp_list:
                write_to_file.write(i)
            
    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('The file will be close')
            print(temp_list)


def main():
    path_in = ('D:\Code\PY\goit-python\HW_07\AP\Files\some_text.txt')
    path_out = ('D:\Code\PY\goit-python\HW_07\AP\Files\some_text_numeric.txt')
    
    to_indexed(path_in, path_out)

if __name__ == '__main__':
    main()


#   write_file.write(line + str(counter) + ': ')