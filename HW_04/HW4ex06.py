"""У нас есть список показателей студентов группы — это список с полученными балами по тестированию. 
Необходимо список поделить на две части. Напишите функцию split_list, которая принимает список (целые числа),
находит среднее значение балла в списке и делит его на два списка. В первый попадают значения меньше среднего, включая среднее значение,
а во второй — строго больше среднего.
Функция возвращает кортеж этих двух списков. Для пустого списка возвращаем два пустых списка.

Функция split_list вернула неправильный результат: None. Должно быть split_list([1, 12, 3, 24, 5]) == ([1, 3, 5], [12, 24])

"""
def split_list(grade):
    #### Считаем среднее 
    sum = 0
    over = []
    under = []
    
    for i in grade:
        sum = sum + i
    try:
        sum = sum // len(grade)
    except ZeroDivisionError:
        x = (under, over)
        return x
    #### делим по признаку
    for i in grade:
        if i <= sum:
            under.append(i)
            
        if i > sum:
            over.append(i)
            
    x = (under, over)
    return x  

print("Rezultat: " , split_list([1, 12, 3, 24, 5]))


"""
def split_list(grade):
    #### Считаем среднее 
    sum = 0
    over = []
    under = []   
    for i in grade:
        sum = sum + i
        try:
            sum = sum // len(grade)
        except ZeroDivisionError:
            return None
    #### делим по признаку
    for i in grade:
        if i <= sum:
            under.append(i)
        if i > sum:
            over.append(i)
    x = (under, over)
    return x

grade_list = (1, 12, 3, 24, 5)

print("YOY OYO Y" , split_list([1, 12, 3, 24, 5]))
#print(sum // len(grade_list))
tmp_list = []
for i in grade_list:
    if type(i) == list:
        for b in i:
            tmp_list.append(b)
    else:
        tmp_list.append(i)
print("Hello ", tmp_list)
"""