"""
Пусть у нас есть текстовый файл, который содержит данные с месячной заработной платой по каждому разработчику компании.

Пример файла:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Как видим, структура файла — это фамилия разработчика и значение его заработной платы, разделенной запятой.

Разработайте функцию total_salary(path) (параметр path - путь к файлу), которая будет разбирать построчно файл и возвращать общую сумму заработной платы всех разработчиков компании.

Требования к задаче:

функция total_salary возвращает значение типа float
для чтения файла функция total_salary использует только метод readline
мы пока не используем менеджер контекста with

"""
def total_salary(path):
    #str_count = 0
    fh = open(path, 'r')
    salary = 0
    while True:
        lines = fh.readline()
        if not lines:
            break
        salary = salary + int(lines[lines.find(',')+1:])
        #str_count = str_count + 1
    #print(salary, str_count)
    fh.close()
    return float(salary)


path = ('D:\Code\PY\goit-python\HW_06\AP\Files\salary.txt')
print(total_salary(path))