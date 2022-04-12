import math

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

D = b ** 2 - 4 * a * c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
else:
    x2 = (-b - math.sqrt(abs(D))) / (2 * a)

    