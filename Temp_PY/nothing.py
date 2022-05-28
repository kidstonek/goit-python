
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


names = ["David", "John", "Annabelle", "Johnathan", "Veronica"]

#your code goes here

for i in names:
    if len(i) > 5:
        print(i)

answer_list = []
for i in filter(lambda x: len(x) > 5, names):
    answer_list.append(i)

print(answer_list, end='')


txt = 'This is some text'


def words(txt):
    bb = txt.split(' ')
    #your code goes here
    for i in range(len(bb)):
        yield bb[i]


print(list(words(txt)))


text = 'some text'


def uppercase_decorator(func):
    def wrapper(text):
        # your code goes here
        ts = str(text.upper())
        return ts
    return wrapper


@uppercase_decorator
def display_text(text):
    return(text)


print(display_text(text))


sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])



def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)


print(fib(4))


a = {'a', 'b', 'c'}
b = {'c', 'd', 'e'}
print(a & b)


nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
print(nums)
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))



def lookup_key(data, value):
    new_lang = []
    for ky_, val_ in data.items():
        if val_ == value:
            new_lang.append(ky_)

    return new_lang

print(lookup_key(lookup_key_yo, 3))

newDict = {key: value for (key, value) in dictOfNames.items() if len(value) == 6 }

lookup_key_yo = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}

#answer = dict(filter(lambda x: x[1] == 2, lookup_key_yo.items())).items() # поиск ключа и значения

for i in dict(filter(lambda x: x[1] == 2, lookup_key_yo.items())).keys():
    print(i)

aa = dict(filter(lambda y: y[0], dict(
    filter(lambda x: x[1] == 2, lookup_key_yo.items()))))

print(aa)



for ch in srtin:
    if ch.isdigit():
        print(ch, end=' ')


srtin = "The resulting profit was: from the southern possessions $ 10, from the northern colonies $50, and the king gave $100."
for i in filter(lambda x: bool(x.isdigit()), srtin):
    print(i)


def input_number():
    while True:
        try:
            num = input("Enter integer number: ")
            return int(num)
        except:
            print(f'"{num}" is not a number. Try again')


num = input_number()


def add_id(id_list: list, employee_id: str):
    if employee_id[:2] != '01':
        return id_list        
    else:
        id_list.append(employee_id)
        return id_list

iddd = []
print(add_id(iddd, '01ee'))


lookup_key_yo = {'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}

newDict = {key for (
    key, value) in lookup_key_yo.items() if  value == 2}

print(newDict)


class Mammal:
    phrase = ''

    def voice(self):
        return self.phrase


class Dog(Mammal):
    phrase = 'Bark!'


class Cat(Mammal):
    phrase = 'Meow!'


class Chupakabra:
    def voice(self):
        return 'Whooooo!!!'


class Recorder:
    def record_animal(self, animal):
        voice = animal.voice()
        print(f'Recorded "{voice}"')


r = Recorder()
cat = Cat()
dog = Dog()
strange_animal = Chupakabra()

r.record_animal(cat)            # Recorded "Meow!"
r.record_animal(dog)            # Recorded "Bark!"
r.record_animal(strange_animal)  # Recorded "Whooooo!!!"
"""

num = 3
def fibonacci(n):
    if n <= 1:
        print(0+n)
        return 1
    else:
        
        return (fibonacci(n - 1)) + fibonacci(n - 2)


fibonacci(num)
