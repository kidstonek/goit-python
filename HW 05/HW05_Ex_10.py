"""
Напишите функцию find_word, которая принимает два параметра: 
первый text и второй word. Функция выполняет поиск указанного слова word в тексте text с помощью функции search и возвращает словарь.

При вызове функции:

print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor 
to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))

Результат должен быть следующего вида при совпадении:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}

где

result — результат поиска True или False
first_index — начальная позиция совпадения
last_index — конечная позиция совпадения
search_string — часть строки, в которой было совпадение
string — строка, переданная в функцию

Если совпадений не обнаружено:

print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))


Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}

"""
import re


def find_word(text, word):
    answer = {}
    find_result =  re.search(word, text)
    if re.search(word, text) != None:
        answer['result'] = True
        #<re.Match object; span=(34, 40), match='Python'>
        answer['first_index'] = find_result.span()[0]
        answer['last_index'] = find_result.span()[1]
        answer['search_string'] = word
        answer['string'] = text

    else:
        answer['result'] = False
        answer['first_index'] = None
        answer['last_index'] = None
        answer['search_string'] = word
        answer['string'] = text    
    return answer


def main():
    search_str = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0."
    print(find_word(search_str,'Python'))



if __name__ == '__main__':
    main()