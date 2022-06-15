#HW4ex02.py
"""
При анализе данных часто возникает необходимость избавиться от экстремальных значений, 
прежде чем начать работать с данными дальше. Напишите функцию prepare_data, которая 
удаляет из переданного списка наибольшее и наименьшее значение, 
сортирует его в порядке возрастания и возвращает измененный список в качестве результата.
"""



def prepare_data(data):
    sort_data = sorted(data)
    print(f"сортируем список {sort_data}")
    
    sort_data.pop(0)
    print(f"удаляем первый элемент {sort_data}")

    sort_data.reverse()
    print(f"разворачиваем список {sort_data}")

    sort_data.pop(0)
    print(f"удаляем первый элемент {sort_data}")
    
    sort_data.reverse()
    print(f"разворачиваем список {sort_data}")   

    return sort_data



data = [1, 3.1415, 41, 3]

print(f"Было до преобразования: {data}")

print(prepare_data(data))