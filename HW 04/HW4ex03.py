"""
Мы разрабатываем кулинарный блог. И в рецептах, при написании списка ингредиентов, мы разделяем их запятыми,
а перед последним ставим союз "и", как в примере ниже:

яйца 2шт, сахар 1 л., соль 1 чл. и уксус

Напишите функцию format_ingredients, которая будет принимать на вход список из ингредиентов и возвращать
собранную строку из его элементов в описанный выше способ. Ваша функция должна уметь обрабатывать списки любой длины.

Ожидалось, что format_ingredients(['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']) == 'яйца 2шт, сахар 1 л., соль 1 чл. и уксус'
"""


def format_ingredients(items):
    answer = ''
    if len(items) <= 0:
        return answer
    if len(items) == 1:
        answer = items[(len(items)-1)]
        return answer 
    if len(items) == 2:
        answer = items[(len(items)-2)] + ' и ' + items[(len(items)-1)]
        return answer
    else:    
        first_part = items[:(len(items)-2)]
        for sd in first_part:
            answer += sd + ', '
        answer = answer + items[(len(items)-2)] + ' и ' + items[(len(items)-1)]
        return answer  

#ingredients = ['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус', 'test']
ingredients = ['яйца 2шт']

#print(ingredients)

print(format_ingredients(ingredients))


"""pos = int([(len(ingredients)-2)])"""
"""ingredients.insert(int([(len(ingredients)-2)])," и ")
print(ingredients)"""

"""sort_ing_min_one = ingredients[:(len(ingredients)-1)]
sort_ing_min_last = ingredients[(len(ingredients)-2)]
print(sort_ing_min_one)
print(sort_ing_min_last)"""

"""tmp = [(len(ingredients)-2)]
print(tmp)"""
"""print(format_ingredients(ingredients))"""

