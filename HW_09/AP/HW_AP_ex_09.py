"""
Вначале четвертого модуля мы решали задачу выплат по коммунальным платежам. Они представляли собой список payment
с положительными и отрицательными значениями. Создайте функцию positive_values и с помощью функции filter отфильтруйте
список payment по положительным значениям, и верните его из функции.
"""


def positive_values(list_payment):
    list_of_positive = []
    for i in filter(lambda x: bool(x > 0), list_payment):
        list_of_positive.append(i)
    return list_of_positive


def main():
    payment = [100, -3, 400, 35, -100]
    print(positive_values(payment))


if '__main__' == __name__:
    main()
