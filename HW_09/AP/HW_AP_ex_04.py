"""
Вернемся к задаче расчета цены с учетом дисконта и разберем подход с позиции каррирования.
Создайте функцию discount_price(discount), которая будет определять в себе и возвращать функцию расчета реальной цены
с учетом скидки.

Вызов функции discount_price(discount) вернет функцию, которая рассчитывает цену на товар со скидкой равной discount.

Например:

cost_15 = discount_price(0.15)
cost_10 = discount_price(0.10)
cost_05 = discount_price(0.05)

price = 100
print(cost_15(price))
print(cost_10(price))
print(cost_05(price))

Должен вывести:

85.0
90.0
95.0

price = price * (1 - discount)
"""


def discount_price(discount):
    def inner(x):
        x = x * (1 - discount)
        return x
    return inner


def main():
    price = 100
    cost_15 = discount_price(0.15)
    print(cost_15(price))



if __name__ == '__main__':
    main()
