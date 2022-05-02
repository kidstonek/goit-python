"""
Задана ведомость абитуриентов, сдавших вступительные экзамены в университет.
Структура данных об абитуриентах представлена в виде следующего списка:

[
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

В каждом словаре данного списка записана фамилия абитуриента — ключ name, код специальности,
на которую он поступает — ключ specialty, и полученные им баллы по отдельным дисциплинам — ключи math (математика),
lang (украинский язык) и eng (английский язык)

Разработайте функцию save_applicant_data(source, output), которая будет указанный список из
параметра source сохранять в файл из параметра output

Структура сохраняемого файла должна быть следующей. В каждой новой строке файла должны быть
записаны через запятую без пробелов фамилия абитуриента, код специальности, на которую он поступает,
и полученные им баллы по отдельным дисциплинам.

Kovalchuk Oleksiy,301,175,180,155
Ivanchuk Boryslav,101,135,150,165
Krapenko Dmitro,201,155,175,185

Требования:

откройте файла output для записи, используя менеджер контекста with и режим w.
запись нового содержимого файла output должна быть или с помощью метода writelines, или использовать метод write

"""
students_list = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

def save_applicant_data(source, output):
    str_list_for_write = []
    
    for students in source:
        string_st = ''
        for students_keys, students_data in students.items():
            if students_keys == "eng":
                #print('NO KEY NEEDED!!!!')
                string_st += str(students_data)
            else:
                string_st += str(students_data) + ','
        string_st = string_st + '\n'
        str_list_for_write.append(string_st)
            
    print(str_list_for_write)
    try:
        with open(output, 'w') as fh:
            fh.writelines(str_list_for_write)
                  
            
    except OSError as err:
            print(f'Ошибка доступа к файлу: {err}')

    finally:
            print('ВсЙО бєнч')
            fh.close() 
        


path_o = ('D:\Code\PY\goit-python\HW_06\AP\Files\output_08.txt')

save_applicant_data(students_list, path_o)