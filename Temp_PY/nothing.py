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

for i , v in x.items():
    print(v)