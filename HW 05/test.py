"""
# такое
num = int(input())

if num % 2 == 0:
  is_even = True
else:
  is_even = False

print(is_even)"""


# разбирался с поиском в строке
"""spam = 'Молох.'
x = 'лох'
print(spam.find(' ' + x))
print(spam.rfind(x +'.'))"""


#Работа с Транслейт и словарем

"""CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.lower())] = l.lower()

print(len(CYRILLIC_SYMBOLS) , len(TRANSLATION))

print("Александр Іванович".translate(TRANS))  # chasha
print("Александр івич".translate(TRANS))  # CHASHA"""

##############################
#######
"""
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

student_s = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
i = 1
for key_s, value_s in student_s.items():
  print('{:>4}|''{:<10} |{:^5} |{:^5}'.format(i, key_s, value_s, grades.get(value_s)))
  i += 1

 """ 
 ################################
 # 
"""print('|{:^10}|{:^10}|{:^10}|'.format('decimal','hex', 'binary'))
for i in range(16):
  s = "|{0:<10d}|{0:^10x}|{0:>10b}|".format(i)
  print(s)"""

"""import re
sttr = 'python'
p = re.sub(sttr, '***', 'blue python and Python shoes', re.IGNORECASE)

print(p)"""
"""
#ищет слова и заменяет их в строке на количество точек
import re
spam = ['began', 'Python', 'and']
search_str = 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn'
for q in spam:
    x = re.findall(q, search_str, re.IGNORECASE)
    for i in x:
      print(i)
      xc = i
      p = re.sub(xc, len(xc) * '*', search_str)
      search_str = p
print(p)"""