"""
Есть две строки в разных кодировках - "utf-8" и "utf-16". Нам необходимо понять, равны ли строки между собой.

Реализуйте функцию is_equal_string(utf8_string, utf16_string), которая возвращает True, если строки равны между собой, и False — если нет.
"""

def is_equal_string(utf8_string, utf16_string):
    
  

    return utf8_string.decode().casefold() == utf16_string.decode('utf-16').casefold()


string_utf8 = 'привет'.encode('utf-8')
string_utf16 = 'привет'.encode('utf-16')

print(is_equal_string(string_utf8, string_utf16))

############################ НЕ УВЕРЕН, ЧТО ТУТ ПРАВИЛЬНО РЕШЕНО !!!!!!!!!!!!!!