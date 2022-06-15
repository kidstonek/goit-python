"""
Есть четырехугольная схема полетов дрона с координатами (1, 2, 3, 4). 
У нас есть словарь points, ключи которого — кортежи, точки полета между координатами четырехугольника, вида (1, 2).
Значения словаря — это расстояния между указанными точками.

points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}

Напишите функцию calculate_distance, которая на вход принимает список координат четырехугольника из словаря вида [0, 1, 3, 2, 0].
Функция должна подсчитать, используя указанный словарь, какое общее расстояние пролетит дрон, двигаясь между точками.

Примечания:

при взятии у словаря points значения, в ключ-кортеже всегда должна быть первой координата с меньшим значением — (2, 3), но не (3, 2);
для пустого списка и списка с одной координатой функция calculate_distance должна возвращать 0.


Answer: Функция calculate_distance вернула неправильный результат: None. Должно быть calculate_distance([0, 1, 3, 2, 0, 2]) == 17.6

"""
points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}
def check_touple(toup):
    if toup[0] > toup[1]:
        x = (toup[1] , toup[0])
        return x
    else:
        return toup

def calculate_distance(coordinates):
    sum = 0
    if coordinates == {} or len(coordinates) == 1:
        return 0
    else:
        for i in range(len(coordinates)-1):
            x = (coordinates[i], coordinates[i+1])
            for indx in points.keys():
                if indx == check_touple(x):
                    sum = sum + points.get((indx))
                
        return sum


coord = [0, 1, 3, 2, 0, 2]


print(calculate_distance(coord))

"""
sum = 0
xx = (2,3)
for indx in points.keys():
    if indx == xx:
        sum = sum + points.get((indx))
        print(points.get((indx)))
"""
#x = (coord.index(0), coord.index(1))


"""for i in range(len(coord)-1):
    x = (coord[i], coord[i+1])
    
x = (4,2)
print(check_touple(x))"""

"""    x = coord[0:2]
    print(x)"""

"""inx = 0
for i in coord:
    if coord.index(inx) > coord.index(inx+1):
        x = (coord.index(inx), coord.index(inx+1))
    else:
        x = (coord.index(inx+1), coord.index(inx))
    inx += 1
    

    print(x)"""

"""for i in coord:
    if coord
    print(i)"""

""" 0 1, 1 3, 3 2, 2 0, 0 2"""
"""i = 0
for val in points.values():
    print(val)"""

"""for ind, val in points:
    if points.values(index(0))
    print(ind)"""

