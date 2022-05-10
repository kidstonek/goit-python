"""
Вернемся к предыдущей задаче и выполним обратную задачу. Напишите рекурсивную функцию encode для кодирования списка или строки.
В качестве аргумента функция принимает список (например ["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"])
или строку (например "XXXZZXXYYYZZ").
Функция должна вернуть закодированный список элементов (пример ["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]).

['X', 3, 'Z', 2, 'X', 2, 'Y', 3, 'Z', 2]
"""


def encode(data):
    if not data:
        return []
    counter = 0
    el = ''
    for i in data:
        if el == '':
            el = i
        if i == el:
            counter += 1
        if i != el:
            break
    return [data[0]] + [counter] + encode(data[counter:])
#от первого елемента + счетчик + список от счетчика

def main():

    daten = ['X', 'X', 'X', 'Z', 'Z', 'X', 'X', 'Y', 'Y', 'Y', 'Z', 'Z']
    print(encode(daten))


if __name__ == '__main__':
    main()


# Без рекурсии
    """
    def encode(data):
    result_list = []
    count = 0
    letter = data[0]
    for el in data:
        if letter == el:
            count += 1
        if letter != el:
            result_list.append(letter)
            result_list.append(count)
            letter = el
            count = 1
    result_list.append(letter)
    result_list.append(count)
    return result_list

    """
