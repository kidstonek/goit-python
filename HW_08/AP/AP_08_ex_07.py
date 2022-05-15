"""
У нас есть именованный кортеж для хранения котов в переменной Cat. На первом месте у нас кличка котика nickname,
потом его возраст age и имя владельца кота owner.

Разработайте функцию convert_list(cats), которая будет работать в двух режимах.

Если функция convert_list принимает в параметре cats список именованных кортежей

[Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

То функция вернет следующий список словарей:

[
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

И в то же время, если функция convert_list принимает в параметре cats список словарей,
то результатом будет обратная операция и функция вернет список именованных кортежей.

Для определения типа параметра cats используйте функцию isinstance.

"""

import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats: {}):
    answer_list = []
    if isinstance(cats[0], Cat): #проверяем является ли список экземпляром именованого списка
        result_data = {}
        for elements in cats:
            result_data["nickname"] = elements.nickname
            result_data["age"] = elements.age
            result_data["owner"] = elements.owner
            answer_list.append(result_data)
            result_data = {}
        return answer_list

    else:
        for i in cats:
            tmp_list = []
            for k, v in i.items():
                tmp_list.append(v)
            answer_list.append(Cat(tmp_list[0], tmp_list[1], tmp_list[2]))

    return answer_list


def main():
    cats_in = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]

    print(convert_list(cats_in))

    ...

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""
    cats_in = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
"""