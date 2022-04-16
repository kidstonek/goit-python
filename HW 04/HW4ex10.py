"""
Браузер Chrome предлагает нам сгенерированные случайные пароли для сайтов и веб-приложений. 
Мы потренируемся решать подобные задачи. Разобьем ее на три этапа. Первый этап — создайте функцию get_random_password,
которая будет генерировать случайную строку пароль.

Требования:

в пароле должно быть 8 символов.
для шифрования пароля будем использовать следующий набор символов:
()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
Эти символы лежат в пределах от 40 до 126 кода в таблице ASCII включительно, и доступ к ним можно получить с помощью функции chr

chr(40)  # (
chr(126)  # ~

Чтобы получить случайное целое значение из заданного диапазона, мы используем стандартный модуль Python random
и его функцию randint. Она имеет вызов вида randint(A, B) и возвращает случайное целое число N, A ≤ N ≤ B.

from random import randint
random_num = randint(40, 126)

После выполнения кода в random_num будет находиться случайное целое число от 40 до 126 включительно.

Таким образом функция get_random_password должна случайным образом выбрать из предложенного диапазона 8 символов
и возвратить сгенерированный пароль в виде строки.
"""

from random import randint


def get_random_password():
    string_psw = ("()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
    random_num = randint(40, 126)
    password = ''
    for i in range(8):
        random_num = randint(40, 126)
        #print(random_num, chr(random_num))
        password = password + chr(random_num)
        i = i + 1
        #print(password)
    return password

print(get_random_password())