"""
Напишите функцию для определения количества дней в конкретном месяце.
Ваша функция должна принимать два параметра: month — номер месяца в виде целого числа в диапазоне от 1 до 12 и year — год,
состоящий из четырех цифр. Убедитесь, что функция корректно обрабатывает февраль високосного года.

"""
import datetime
from datetime import date


def get_days_in_month(month, year):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]
    current_datetime_1 = datetime.date(year=year, month=month, day=1)
    current_datetime_2 = datetime.date(year=year+1, month=month, day=1)
    print(current_datetime_2 - current_datetime_1)
    if month in days_31:
        return 31
    if month in days_30:
        return 30
    if str('366') in str(current_datetime_2 - current_datetime_1):
        return 29
    else:
        return 28



def main():
    month_in = 2
    year = 2021
    print(get_days_in_month(month_in, year))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
