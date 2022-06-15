"""
В модуле работы с функциями мы писали функцию get_fullname для составления полного имени. Выполним небольшое продолжение задачи и напишем функцию is_check_name, 
которая принимает два параметра (fullname, first_name) и возвращает логическое True или False. Это результат проверки, является ли строка first_name префиксом строки fullname.
Функция is_check_name строго относится к регистру букв, то есть «Sam» и «sam» для неё разные имена.


Функция работает неправильно и возвращает: None. Должно быть is_check_name('Alex Old', 'Alex') == True

"""

def is_check_name(fullname, first_name):
    if first_name in fullname:
        return True
    return False


def main():
    print(is_check_name('Alex Old', 'alex'))
    

if __name__ == '__main__':
    main()