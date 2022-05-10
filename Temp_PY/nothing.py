import re
x = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
}
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

data = ['X', 'X', 'X', 'Y']
kol_vo = 0
for i in range(len(data)):
    el = data[i]
   
    kol_vo += 1
print(kol_vo)




"""def factorial(num):
    if num == 1:
        return 1
    num = num * factorial(num-1)
    return num

print(factorial(4))"""

