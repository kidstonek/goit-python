from datetime import date, datetime
from pstats import SortKey
import re
"""x = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}"""
"""p = re.sub(r':', ' =', str(x))
print(x)
print(p)"""

"""for i , v in x.items():
    print(v)"""

"""stt = "lick my balls you!"
print(stt.find('balls'))

if 'ballz' in stt:
    print("YO")

s = 'ballz '

print(s.lstrip())"""

"""data = ['X', 'X', 'X', 'Y']
kol_vo = 0
for i in range(len(data)):
    el = data[i]
   
    kol_vo += 1
print(kol_vo)
"""


"""def factorial(num):
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
"""
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
