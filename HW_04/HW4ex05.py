"""Как мы уже знаем, ключ в словаре должен быть уникальным, а вот значение его нет.
 Реализуйте функцию lookup_key для поиска всех ключей по значению в словаре.
 Первым параметром в функцию мы передаем словарь, а вторым — значение, которое хотим найти.
 Таким образом результат может быть как список ключей, так и пустой список, если мы ничего не найдем."""

def lookup_key(data, value):
    new_lang = []
    for ky_, val_ in data.items():
        if val_ == value:
            new_lang.append(ky_)
            
    return new_lang

lookup_key_yo = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}

    
"""    value2 = 2
    for l, value2 in lookup_key_yo.items():
    print(f"Programming language {l} - released {value2}")"""

print(lookup_key(lookup_key_yo, 2))

"""lang = {"Python": 1991, "Java": 1995, "JS": 1995}
for l, value in lookup_key_yo.items():
    if l == "key1":
        print("опа опа")
    print(f"Programming language {l} - released {value}")"""