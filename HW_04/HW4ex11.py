"""
Второй этап. Необходимо написать функцию is_valid_password, которая будет проверять полученный параметр — пароль на надежность.

Критерии надежного пароля:

Длина строки пароля восемь символов.
Содержит хотя бы одну букву в верхнем регистре.
Содержит хотя бы одну букву в нижнем регистре.
Содержит хотя бы одну цифру.
Функция is_valid_password должна вернуть True, если переданный в качестве параметра пароль отвечает требованиям надежности. В противном случае вернуть False.

()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~

"""

def is_valid_password(password):
    numbers_list = '0123456789'
    dict_up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    dict_low_letters = 'abcdefghijklmnopqrstuvwxyz'
    if len(password) < 8:
        return False
    tmp_pass = set(password) & set(dict_up_letters)
    if tmp_pass == set():
        return False
    tmp_pass = set(password) & set(numbers_list)
    if tmp_pass == set():
        return False
    if tmp_pass == set():
        return False
    tmp_pass = set(password) & set(dict_low_letters)
    if tmp_pass == set():
        return False

    return True


p = 'D@#Fwrtf54'
print(is_valid_password(p))

"""#x = set(x)
numbers_list = [0,1,2,3,4,5,6,7,8,9]
dict_up_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dict_low_letters = 'abcdefghijklmnopqrstuvwxyz'
y = set(p) & set(dict_up_letters)
if y == set():
    print('Пусто')
print(y)"""