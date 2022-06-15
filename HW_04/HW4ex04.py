"""Реализуйте две функции. Первая будет использоваться в бухгалтерии при расчете стипендии, 
get_grade принимает ключ в оценке ECTS, и должна возвращать соответствующую пятибалльную оценку (первый столбик таблицы). 
Вторая get_description тоже принимает ключ в оценке ECTS, но будет возвращать объяснение оценки в текстовом формате (последний столбик таблицы)
 и будет использоваться в электронной зачетке студента. 
На несуществующий ключ функции должны возвращать значение None."""

def get_grade(key):
    try:
        grade_dict[key]
    except KeyError:
        return None
    return grade_dict[key]
    
    


def get_description(key):
    try:
        grade_dis_dict[key]
    except KeyError:
        return None
    return grade_dis_dict[key]


grade_dict = {
    "F": 1,
    "FX": 2,
    "E": 3,
    "D": 3,
    "C": 4,
    "B": 5,
    "A": 5
}

grade_dis_dict = {
    "F": "неудовлетворительно",
    "FX": "неудовлетворительно",
    "E": "достаточно",
    "D": "удовлетворительно",
    "C": "хорошо",
    "B": "очень хорошо",
    "A": "отлично"
}

print(get_grade("A"))