"""
Напишите функцию parse_folder, она принимает единственный параметр path,
который является объектом Path. Функция должна просканировать директорию path и вернуть кортеж из двух списков.
Первый — это список файлов внутри директории, второй — список директорий.

Пример вывода функции:

(['.gitignore', 'readme.md'], ['.git', '.idea', '.vscode', 'module-01', 'module-02', 'module-03', 
'module-04', 'module-05', 'module-06', 'module-07', 'module-08', 'module-09', 'module-10', 'module-11', 'module-12'])

"""
from pathlib import Path


def parse_folder_old(path):
    files = []
    folders = []
    for i in path.iterdir():
        files.append(i.name)
    for i in path.parts:
        """if i == path.drive:
            break"""
    folders.append(i)
    x = (files, folders)
            
    return x

def parse_folder(path):
    files = []
    folders = []
    for i in path.iterdir():
        if i.is_dir() == True:
            print(f'папка {i.name}')
            folders.append(i.name)
        else:
            files.append(i.name)
            print(f'файл - {i.name}')
    x = (files, folders)
            
    return x

p = Path('D:\\Files to delete\\Счета\\Vodafone\\2022')
print(parse_folder(p))
#ttt = []

# Идем по папке и проверяем это каталог или папка
"""for i in p.iterdir():
    if i.is_dir() == True:
        print(f'папка {i.name}')
    else:
        print(f'файл - {i.name}')"""
    

#вывод файлов в папке Path
"""for i in p.iterdir():
    ttt.append(i.name)
    print(i.name)
print(ttt)"""

"""for i in p.parts:
    ttt.append(i)

print(ttt)"""

"""for i in p.iterdir():
    ttt.append(i)
    #print(i.parents)
#print(ttt)
print(p, p.parent)"""
