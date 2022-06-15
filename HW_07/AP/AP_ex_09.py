"""
Подсписком (sublist) называют список, являющийся составной частью большего списка. Подсписок может содержать один элемент, множество элементов, а также быть пустым.

Например, [1], [2], [3] и [4] являются подсписками списка [1, 2, 3, 4]. Список [2, 3] также входит в состав [1, 2, 3, 4], 
но при этом список [2, 4] не является подсписком [1, 2, 3, 4], поскольку в исходном списке числа 2 и 4 не соседствуют.

Пустой список является подсписком для любого списка.

Напишите функцию all_sub_lists, возвращающую список, содержащий все возможные подсписки заданного.

Например, если функции передан аргумент список [1, 2, 3], 
то функция должна вернуть следующий список: [[], [1], [2], [3], [1, 2], [2, 3], [1, 2, 3]]
                                            [[], [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]].

Функция all_sub_lists должна возвращать как минимум один список с пустым подсписком [[]].

"""

def all_sub_lists(data):
    list_of_lists = []
    if data == []:
        list_of_lists.append([])
        return list_of_lists
    else:
        list_of_lists.append([])
        for pos_element in range(len(data)+1):
            for el_list in range(len(data)+1):
                if pos_element < el_list:
                    list_of_lists.append(data[pos_element:el_list])
    return sorting_list(list_of_lists)

def sorting_list(list_for_sort:list) -> list:
    mega_sorted_list = []
    for i in range(len(list_for_sort)):
        for b in list_for_sort:
            if len(b) == i:
                mega_sorted_list.append(b)
    return mega_sorted_list        
        

def main():
   input_list = [1, 2, 3]
   print(all_sub_lists(input_list))
   #print(sorting_list(sort_test))

if __name__ == '__main__':
    main()