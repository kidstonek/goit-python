"""

try:
        with open(path, 'r') as fh:
            
                  
            
    except OSError as err:
        print(f'Ошибка доступа к файлу: {err}')

    finally:
        print('ВсЙО бєнч')
        fh.close()  





strr = 'Nikita Borisenko,2000'

tmp_dig = ''
answer = 0

tmp_dig = strr[strr.find(',')+1:]
for i in strr:
    if i in '1234567890':
        #print('ok')
        tmp_dig = tmp_dig + i

#answer = answer + int(tmp_dig)
print(tmp_dig)    """

### for 4 ex
"""emp_list = [['Robert Stivenson,28', 'Alex Denver,30'],['Drake Mikelsson,19']]

for i in emp_list:
    #if type(i) == list:
        for k in i:
            print(k)
        """

### for 5 ex
"""
test_cat = '60b90c4613067a15887e1ae5,Tessi,5'

print(test_cat.split(','))

for i in test_cat.split(','):
    print(i)

a = []
b = {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"}
c = {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"}

a.append(b)
a.append(c)
print(a)

#for ex 6

ttt = {}
if ttt == {}:
    print( "Пусто")
    """
# for ex 7
"""
sss = 'Drake Miel, 24'
return_s = ''

for i in sss:
    if i in '1234567890':
        continue
    else:
        return_s = i + return_s
print(return_s[::-1])


# for 8
students_list = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]
one_st =     {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    }

listt = []
string_st = ''
for i in students_list:
    string_st = ''
    for k, v in i.items():
        if k == 'eng':
            print('Fucking eng!')
            string_st += str(v)
        else:
            string_st += str(v) + ', '
        #print(v)
    listt.append(string_st)
    #print(string_st)
print(listt)

# for ex 9 
s = "Привет!"
utf8 = s.encode('utf-8')
utf16 = s.encode('utf-16')
print(utf8)
""" 

# for ex 10

"""users_info = {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
code_str = ''
for u_key, u_val in users_info.items():
    code_str = u_key + ':' + u_val
    print(code_str.encode('utf-16'))
    print(u_key + ':' + u_val)
"""

"""x = input()

elements = x.split()
if elements.count(x) == 1:
    print(x)
else:
    x = x[::-1]
    print(x[0])

#print(elements.count(x))
#print(elements[::-1])"""


"""x = int(input()) 
#your code goes here
answer=[i*(5*3) for i in range(x) if i*(5*3) < x]


print(answer)

evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)"""

"""name = input()
age = int(input())

#your code goes here
print('{name} is {age} years old'.format(name = name, age = age))"""

import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name: str) -> str:  
    p_name= name.translate(TRANS)
    t_name = name.translate(TRANS)
    p_name = re.findall(r'^[^.]+', p_name)
    p_name = re.sub(r'\W', '_', p_name[0])
    t_name = re.sub(r'^[^.]+', '', t_name)
    return p_name + t_name

file_name = 'te!#,а%$424ва.py'

print(normalize(file_name))