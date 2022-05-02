"""
Разработайте функцию sanitize_file(source, output), переписывающую в текстовый файл output
содержимое текстового файла source, очищенное от цифр.

Требования:

прочтите содержимое файла source, используя менеджер контекста with и режим "r".
запишите новое очищенное от цифр содержимое файла output, используя менеджер контекста with и режим "w"
запись нового содержимого файла output должна быть единоразовая и использовать метод write
"""

def sanitize_file(source, output):
    all_in_one = ''
    try:
        with open(source, 'r') as fh_s:
            
                temp_str = '' 
                while True:
                    
                    lines = fh_s.readline()
                    for line in lines:
                        for ch in line:
                            if ch not in '1234567890':
                                temp_str = ch + temp_str
                                temp_str = temp_str.strip('\n')
                    all_in_one = str(temp_str[::-1])
                    """fh_o.write(all_in_one)
                    temp_str = ''
                    print(all_in_one)"""
                    if not lines:
                        break
        with open(output, "w") as fh_o: # запись в файл
            fh_o.write(all_in_one)          
                  
            
    except OSError as err:
        print(f'Ошибка доступа к файлу: {err}')

    finally:
        print('ВсЙО бєнч')
        fh_s.close()
        fh_o.close()

    

path_s = ('D:\Code\PY\goit-python\HW 06\AP\Files\\test_07.txt')
path_o = ('D:\Code\PY\goit-python\HW 06\AP\Files\ex_07_output.txt')

sanitize_file(path_s, path_o)


#Красивая альтернатива
""" 
def sanitize_file(source, output):
    with open(source, 'r') as f:
        text = f.read()
    new_text = ''
    for ch in text:
        if not ch.isdigit():
            new_text += ch
    with open(output, 'w') as f:
        f.write(new_text)
"""