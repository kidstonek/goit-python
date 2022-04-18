"""
Создайте функцию parse_args, которая возвращает строку, составленную из аргументов командной строки, разделенных пробелами.
Например, если скрипт был вызван командой:
python run.py first second, то функция parse_args должна вернуть строку следующего вида "first second".
"""

from os import path
import sys


def parse_args():
    result = ''
    my_param = sys.argv[1:len(sys.argv)]
    for x in range(len(my_param)):
        result = result + " " + my_param[x]
       # print(my_param[x])
    x = result.lstrip()    
                 
    return x
    
                 



"""result = ''
per = len(sys.argv) - 1

for i in range(per):
    if i == 0:
        continue
    result = str(sys.argv[i]) + ' ' + result
    
for i in result[6::-1]:
    per = i + " " + per
print(per)   
    
"""
print(parse_args())