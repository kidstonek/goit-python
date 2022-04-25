"""
Для закрепления материала напишите функцию find_all_words, которая ищет совпадение слова в тексте.
Функция возвращает список всех нахождений слова в параметре word в тексте в любом виде написания, т.е. например,
возможные варианты написания слова "Python" как pYthoN, pythOn, PYTHOn и т.д. главное, чтобы сохранялся порядок слов,
регистр не имеет значение.

Подсказка: функции модуля re принимают еще последний параметр flags и мы можем определить нечувствительность к регистру,
присвоив ему значение re.IGNORECASE


Функция find_all_words возвращает неправильный результат: []. 
Ожидалось, что при вызове функции find_all_words('Guido van Rossum began working on Python in the late 1980s, 
as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn ', 
'Python') будет получен следующий результат ['Python', 'PYTHOn', 'pYthoN', 'Python', 'pythOn']
"""


import re


def find_all_words(text, word):
    return re.findall(word, text, re.IGNORECASE)

def main():
    search_str = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn "
    print(find_all_words(search_str, 'python'))



if __name__ == '__main__':
    main()