"""
Реализуйте функцию add_employee_to_file(record, path), которая в файл 
(параметр path - путь к файлу) будет добавлять сотрудника (параметр record)
в виде строки "Drake Mikelsson, 19".

Требования:

параметр record - сотрудник в виде строки вида "Drake Mikelsson, 19"
каждая запись в файл должна начинаться с новой строки.
необходимо, чтобы старая информация в файле тоже сохранялась, поэтому при работе с файлом,
откройте файл в режиме "a", добавьте сотрудника record в файл и закройте его
мы пока не используем менеджер контекста with

"""

def add_employee_to_file(record, path):
    fh = open(path, 'a')
    fh.write(record + '\n')
    fh.close()
    

path = ('D:\Code\PY\goit-python\HW 06\AP\Files\employees_add.txt')
employee = 'Drake Miel, 24'

add_employee_to_file(employee, path)