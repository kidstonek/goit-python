"""
Разработайте функцию get_str_date(date),
которая будет преобразовывать дату из базы данных в формате ISO "2021-05-27 17:08:34.149Z"
в строковое представление "Thursday 27 May 2021" — день недели, число, месяц и год.
Преобразованное значение функция должна вернуть при вызове.

"""
from datetime import datetime


def get_str_date(date):
    pretty_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%fZ') # преобразование в строку с дибильным форматом
    answer_date = pretty_date.strftime('%A %d %B %Y') # форматирование строки как хотим
    return answer_date



def main():
    my_date = '2021-05-27 17:08:34.149Z'
    print(get_str_date(my_date))


    ...


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
