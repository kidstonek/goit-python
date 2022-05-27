"""
Создайте класс NumberString, наследуйте его от класса UserString, определите для него метод number_count(self),
который будет считать количество цифр в строке.
"""
from collections import UserString


class NumberString(UserString):
    def number_count(self):
        summ = 0
        for i in filter(lambda x: bool(x.isdigit()), self.data):
            summ += 1
        return summ


def main():
    srtin = "The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, " \
            "and the king gave $100."
    num_count = NumberString(srtin)
    print(num_count.number_count())


if '__main__' == __name__:
    main()