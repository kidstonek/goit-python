"""
Перепишем задачу расчета задолженностей по коммунальным услугам с помощью класса UserList.
payment = [1, -3, 4]

def amount_payment(payment):
    sum = 0
    for value in payment:
        if value > 0:
            sum = sum + value
    return sum

Напомним условие. У нас есть список показаний задолженностей по коммунальным услугам
в конце месяца — список payment. Задолженности могут быть отрицательными — у нас переплата, или положительными,
если необходимо оплатить по счетам.

Создайте класс AmountPaymentList, наследуйте его от класса UserList.
Сделайте функцию amount_payment методом класса LookUpKeyDict.

"""
from collections import UserList


class AmountPaymentList(UserList):
    def amount_payment(self):
        sums = 0
        for val in self.data:
            if val > 0:
                sums = sums + val
        return sums


def main():
    payment = [1, -3, 4]
    my_dept = AmountPaymentList(payment)
    print(my_dept.amount_payment())


if '__main__' == __name__:
    main()