articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


dicty = "Name"
word = ''

"""print(dicty.lower())
dict_tmp = {}"""

#перевод в нижний регистр списка
for i in articles_dict:
    string = str(i).lower()
   
    print(string)

"""if word in dict:
    print('нашлось')"""

"""for i in dict.items():
    if dicty in str(i):
       print('Есть вхождение')
    else:
        print(f' {dicty} нет в', i)
    #print(k, i)
    #print(word.find(str(i)))"""


dict1 = {'one':1, 'two':2, 'three': {'three.1': 3.1, 'three.2': 3.2 }}
str1 = str(dict1)

dict2 = eval(str1)

print (dict1 ==dict2)

