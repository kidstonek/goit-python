"""
поиск в тексте гиперссылок.

Напишите регулярное выражение для функции find_all_links, которая будет в тексте (параметр text) находить все линки и
возвращать список полученных из текста совпадений.

В целях упрощения примем, что:

начало гиперссылки может быть http:// или https://
доменное имя — это набор латинских букв, цифр, символов подчеркивания _ и точек .
символы точек . не могут встречаться рядом
Фактически в учебном примере мы будем искать простые url адреса:

https://www.google.com
https://www.facebook.com
https://github.com

Данное регулярное выражение ни в коей мере не претендует на покрытие всех возможных вариантов гиперссылок.

При выполнении этого задания мы рекомендуем использовать следующий сервис для проверок регулярных выражений regex101.

"""
import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r"[https?]{4,5}[\://\\]+[\w]+[\.][\w]+[\.w][\w]+|[https?]{4,5}[\://\\]+[\w]+[\.][\w]+", text)
    for match in iterator:
        result.append(match.group())
    return result


def main():
    all_linx = 'The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com '
    print(find_all_links(all_linx))


if __name__ == '__main__':
    main()