"""
Напишите функцию parse_folder, она принимает единственный параметр path,
который является объектом Path. Функция должна просканировать директорию path и вернуть кортеж из двух списков.
Первый — это список файлов внутри директории, второй — список директорий.

Пример вывода функции:

(['.gitignore', 'readme.md'], ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 
'module-04', 'module-05', 'module-06', 'module-07', 'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])

"""
from pathlib import Path
from tkinter import Y

def parse_folder(path):
    files = []
    folders = []
    for i in p.iterdir():
        files.append(i.name)
            
    
            
    return files, folders

p = Path('C:\\Users\\ava\\Downloads')
#print(parse_folder(p))
ttt = []



#вывод файлов в папке Path
"""for i in p.iterdir():
    ttt.append(i.name)
    print(i.name)
print(ttt)"""

print(p, p.parent)
y = p.parent
print(y, y.parent)
x = y.parent
print(x, x.parent)
y = x.parent
print(y, y.parent)
"""for i in p.iterdir():
    ttt.append(i)
    #print(i.parents)
#print(ttt)
print(p, p.parent)"""
