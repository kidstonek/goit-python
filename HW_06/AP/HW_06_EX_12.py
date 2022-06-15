"""
Функция get_credentials_users из предыдущей задачи возвращает нам список строк username:password:

['andry:uyro18890D', 'steve:oppjM13LL9e']

Реализуйте функцию encode_data_to_base64(data), которая принимает в параметре data указанный список,
выполняет кодирование каждой пары username:password в формат Base64 и возвращает список с закодированными

парами username:password в виде:

['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

"""

import base64


def encode_data_to_base64(data):
    coded_list = []
    for user_data in data:
        user_data_bytes = user_data.encode('utf-8')
        base64_data = base64.b64encode(user_data_bytes)
        base64_user_data = base64_data.decode('utf-8')
        coded_list.append(base64_user_data)

    return coded_list


decoded_list = ['andry:uyro18890D', 'steve:oppjM13LL9e']

print(encode_data_to_base64(decoded_list))