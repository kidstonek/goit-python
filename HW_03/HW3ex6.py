"""Создайте функцию  format_string для форматирования строки. В функцию мы передаем строку
 string и length длину новой строки. Функция возвращает новую строку по следующему алгоритму:

Если длина исходной строки больше или равна length, мы возвращаем ее в том же виде;
Если она меньше length, мы добавляем впереди строки пробелы в количестве (length - len(string)) // 2.
Тесты на правильность работы функции выполняются для следующих наборов аргументов:

string='aaaaaaaaaaaaaaaaac', length=12
length=15, string='abaa'"""

def format_string(string, length):
    if len(string) >= length:
        return string
    else:
        x = (int((length - len(string))) // 2) 
        x = (x * " ") + string
        return x