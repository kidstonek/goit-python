"""
Есть список IP адресов:

IP = [
    "85.157.172.253",
    ...
]

Реализуйте две функции. Первая get_count_visits_from_ip с помощью Counter будет возвращать словарь, где ключ — это IP,
а значение — количество вхождений в указанный список.

Пример:

{
    '85.157.172.253': 2,
    ...
}

Вторая функция get_frequent_visit_from_ip возвращает кортеж с наиболее часто встречаемым в списке IP
и количеством его вхождений в список.

Пример:

('66.50.38.43', 4)
"""
import collections
from collections import Counter


def get_count_visits_from_ip(ips):
    return collections.Counter(ips)


def get_frequent_visit_from_ip(ips):
    most_ips = collections.Counter(ips)
    return most_ips.most_common()[0]


def main():
    ip_list_wo_c = ['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245',
                    '66.50.38.43', '248.95.93.236', '248.95.93.236']
    ip_list_w_c = {'85.157.172.253': 2, '143.231.49.229': 1, '173.37.214.238': 2, '27.137.126.114': 1,
                   '76.98.129.245': 3, '66.50.38.43': 4, '248.95.93.236': 1}

    print(get_count_visits_from_ip(ip_list_wo_c))
    print(get_frequent_visit_from_ip(ip_list_w_c))

    ...

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""
{'85.157.172.253': 2, '143.231.49.229': 1, '173.37.214.238': 2, '27.137.126.114': 1, '76.98.129.245': 3, '66.50.38.43': 4, '248.95.93.236': 1}
['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245', '66.50.38.43', '248.95.93.236']
"""