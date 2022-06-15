"""
Создайте функцию decimal_average(number_list, signs_count), которая будет вычислять среднее арифметическое типа Decimal с количеством значащих цифр signs_count.

number_list — список чисел
============================
Внимание
Не забывайте приводить все числа в списке к типу `decimal`
============================

Пример:

вызов функции decimal_average([3, 5, 77, 23, 0.57], 6) вернет 21.714
вызов функции decimal_average([31, 55, 177, 2300, 1.57], 9) вернет 512.91400

"""

from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    all_ = 0
    getcontext().prec = signs_count
    for n in number_list:
        all_ = Decimal(all_) + Decimal(n)

    return all_ / Decimal(len(number_list))


def main():
    number_list_in = [31, 55, 177, 2300, 1.57]
    signs_count_in = 9
    print((decimal_average(number_list_in, signs_count_in)))


# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
