"""
Вернемся к нашей первой задаче с четвертого модуля и перепишем ее с помощью функции reduce.
payment = [1, -3, 4]


def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum

Напомним условие. У нас есть список показаний задолженностей по коммунальным услугам в конце месяца — список payment.
Задолженности могут быть отрицательными — у нас переплата, или положительными, если необходимо оплатить по счетам.
С помощью reduce просуммируйте положительные значения и сумму платежа в конце месяца верните из функции amount_payment.
"""


from functools import reduce


def amount_payment(payment):
    payment_out = reduce(lambda x, y: x + y, filter(lambda x: bool(x > 0), payment))
    return payment_out


def main():
    payment_in = [1, -3, 4]
    print(amount_payment(payment_in))

if '__main__' == __name__:
    main()
