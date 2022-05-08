"""
В четвертом модуле мы решали задачу нормализации данных. Давайте расширим ее. 
При анализе данных часто возникает необходимость избавиться от экстремальных значений, 
прежде чем начать работать с данными дальше. Напишите функцию data_preparation, которая принимает набор данных,
список списков (Пример: [[1,2,3],[3,4], [5,6]]). 
Функция должна удалять из переданных списков наибольшее и наименьшее значение,
но только если размер списка больше двух элементов. После удаления данных из каждого списка,
необходимо слить их вместе в один список, отсортировать его в порядке убывания и вернуть
полученный список в качестве результата (
Для примера выше результат будет следующим: [6, 5, 4, 3, 2])

"""

def data_preparation(list_data:list):
    list_answer = []
    list_answer_unsort = []
    for i in list_data:
        if len(i) > 2:
            i.remove(max(i))
            i.remove(min(i))
        for b in i:
            list_answer_unsort.append(b)
    for n in range(len(list_answer_unsort)):
        list_answer.append(max(list_answer_unsort))
        list_answer_unsort.remove(max(list_answer_unsort))
    return list_answer




def main():
    data = [[1, 2, 3, 0], [3], [5, 6, 1, 7, 2]]
    print(data_preparation(data))

if __name__ == '__main__':
    main()

