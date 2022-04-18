def get_grade(key):
    grade = {"F": 1, "FX": 2, "E":3, "D":4, "C":5, "A":5,}  
    return grade[key]


def get_description(key):
    description= {"F": 'неудовлетворительно', "FX": 'неудовлетворительно', "E":'достаточно', "D":'удовлетворительно', "C":'хорошо', "B":'очень хорошо',"A":'отлично'}
    return description[key]


print(get_description("B"))

"""
Roman  1 д. назад
get(key[, default]) — не вызывает исключения, если ключа нет в словаре, возвращает default, по умолчанию default=None
grade = grade_dict.get(key, None)
    return grade
"""