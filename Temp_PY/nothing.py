from datetime import date, datetime
from pstats import SortKey
import re
from webbrowser import get
"""x = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
p = re.sub(r':', ' =', str(x))
print(x)
print(p)

for i , v in x.items():
    print(v)

stt = "lick my balls you!"
print(stt.find('balls'))

if 'ballz' in stt:
    print("YO")

s = 'ballz '

print(s.lstrip())

data = ['X', 'X', 'X', 'Y']
kol_vo = 0
for i in range(len(data)):
    el = data[i]
   
    kol_vo += 1
print(kol_vo)



def factorial(num):
    if num == 1:
        return 1
    num = num * factorial(num-1)
    return num

print(factorial(4))

cats_in = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]

for i in cats_in:
    print(i)

def sort_week(week_dict:dict):
    sorted_dict = {}
    weeknds_guys = ''
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in week:
        for days_k, names_v in week_dict.items():
            if day == days_k:
                if days_k == 'Saturday' or days_k == 'Sunday':
                    weeknds_guys = weeknds_guys + ' ' + names_v
                    continue
                sorted_dict[day] = names_v
            if weeknds_guys != '':
                sorted_dict['next Monday'] = weeknds_guys.lstrip()
    #print(weeknds_guys.lstrip())
    return sorted_dict


tmp_dict = {}
birthday_dict = [{'Monday': 'Valera'}, {'Sunday': 'Billy'}, {'Tuesday': 'James'},
                 {'Monday': 'Olga'}, {'Saturday': 'Tetiana'}]

for i in birthday_dict:
    tmp_b_day = ''
    day_of_week = ' '.join(map(str, list(i.keys())))
    for ii in birthday_dict:
        if ii.keys() == i.keys():
            tmp = ''.join(map(str, list(ii.values())))
            tmp_b_day = tmp_b_day + ' ' + tmp
    for b in birthday_dict:
        if day_of_week in b:
            b.pop(day_of_week)
    if day_of_week == '':
        continue
    tmp_dict[day_of_week] = tmp_b_day.lstrip()
print(sort_week(tmp_dict))
###======================================


customers = {"name": "Boris", "discount": 0.15}

print(customers.get("discount"))

def format_phone_number(func):
    def wrapper(phone):
        result = func(phone)
        if len(result) < 12:
            return '+38' + result
        if len(result) == 12:
            return '+' + result
    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


print(sanitize_phone_number('0503451234'))


srtin = "The resulting profit was: from the southern possessions $ 100 , from the northern colonies $500, and the king gave $1000."

bb = srtin.replace('.', '').replace(',', '').replace('$', '').split()
print(bb)
for i in bb:
    if i.isdigit():
        print(type(i))


name = 'andrii'

print(name.capitalize())



data_list = [
    {'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk',
     'phone': '(992) 914-3792', 'favorite': False},
    {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca',
     'phone': '(294) 840-6685', 'favorite': False},
    {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038',
     'favorite': False},
    {'name': 'Wylie Pope', 'email': 'est@utquamvel.net',
     'phone': '(692) 802-2949', 'favorite': False},
    {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}]

for i in data_list:
    print(i.get('email'))
    """

test_dict = {'name': 'Wylie Pope', 'email': 'est@utquamvel.net',
             'phone': '(692) 802-2949', 'favorite': False}


t_dict = {'asdsa': '213123', 'asdssa': 'asd', 'A': '2312312', 'B': '123123123'}
a = 'A'
for k in t_dict.keys():
    if k == a:
        print('ohh way')
        break

for i in filter(lambda x: bool(x == a) == False, t_dict.keys()):
    print(f'{i} = a')


