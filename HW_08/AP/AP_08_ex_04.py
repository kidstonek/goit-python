"""
Для того чтобы выиграть главный приз лотереи, необходимо совпадение нескольких номеров на лотерейном билете с числами,
выпавшими случайным образом и в неком диапазоне во время очередного тиража. Например, необходимо угадать шесть чисел от 1 до 49 или пять чисел от 1 до 36 и т.д.

Напишите функцию, которая будет случайным образом подбирать набор чисел для лотерейного билета. Среди этих чисел не должно быть дубликатов.

Формат функции get_numbers_ticket(min, max, quantity), где параметры:

min — минимальное значение диапазона, не может быть меньше 1
max — максимальное значение диапазона, не может быть большее 1000
quantity — количество чисел в наборе (должен быть min < quantity < max)
Функция должна вернуть список случайных чисел по возрастанию. Если нарушены условия ограничений на параметры функции, тогда вернуть пустой список.

"""
import random
from random import randrange


def get_numbers_ticket(min, max, quantity):
    return_list = []
    if min < 1 or max > 1000:
        return []
    if min > quantity or quantity > max:
        return []
    else:
        while len(return_list) != quantity:
            tmp_i = random.randint(min, max)
            if tmp_i in return_list:
                continue
            else:
                return_list.append(tmp_i)
        res = return_list.sort()
        return return_list


def main():
    min_in = 1
    max_in = 1000
    quantity_in = 26
    print(get_numbers_ticket(min_in, max_in, quantity_in))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
