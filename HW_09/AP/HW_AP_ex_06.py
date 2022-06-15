"""
Пусть есть строка с числами (в целях упрощения числа только целые), определяющая какие-то части общего дохода. Например,
"The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."

Необходимо реализовать функцию generator_numbers, которая будет парсить строку и находить все целые числа в ней,
и работая как генератор, отдавать указанные числа при обращении к ней в цикле.

С парсингом строки мы уже сталкивались в задаче модуля 7, когда разбивали на лексемы арифметическое выражение

Функция generator_numbers(string="") непосредственно распарсивает строку и при помощи yield возвращает текущее число.

Функция sum_profit(string) суммирует числа, полученные от generator_numbers, и возвращает общую сумму прибыли из строки.
"""


def generator_numbers(string=""):
    bb = string.replace('.', '').replace(',', '').replace('$', '').split()
    i = 0
    while i < len(bb):
        if bb[i].isdigit():
            yield bb[i]
        i += 1


def sum_profit(string):
    total_sum = 0
    some_gen = generator_numbers(string)
    for i in some_gen:
        total_sum = total_sum + int(i)
    return total_sum

def main():
    srtin = "The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."
    print(sum_profit(srtin))


if __name__ == '__main__':
    main()
