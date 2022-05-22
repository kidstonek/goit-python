"""
Бот принимает команды:
"hello", отвечает в консоль "How can I help you?"

"add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт. Вместо ... пользователь вводит
имя и номер телефона, обязательно через пробел.

"change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
Вместо ... пользователь вводит имя и номер телефона, обязательно через пробел.

"phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
Вместо ... пользователь вводит имя контакта, чей номер нужно показать.

"show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.

"good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того,
как выведет в консоль "Good bye!".
"""

MY_PHONEBOOK = {}


def input_error(in_func):
    def wrapper(*args):
        try:
            check = in_func(*args)
            print(check)
        except KeyError:
            return print('There is no such a contact. Please try again')
        except IndexError:
            return print('Give me name and phone please')
        except ValueError:
            return print('ValueError')
        except TypeError:
            return print('TypeError')
    return wrapper


@input_error
def handler_adder(add_string: str):
    tmp = str(add_string.split(' ')[1])
    for i in filter(lambda x: bool(x == tmp), MY_PHONEBOOK.keys()):
        return "Such a name already exists. Please try again"
    if str(add_string.split(' ')[1]).isdigit() or str(add_string.split(' ')[1]) == '':
        return "Incorrect user name. Try again"
    if not str(add_string.split(' ')[2]).isdigit() or str(add_string.split(' ')[2]).isdigit() == '':
        return "Incorrect phone number. Try again"
    MY_PHONEBOOK[str(add_string.split(' ')[1])] = str(add_string.split(' ')[2])
    return 'Contact ' + str(add_string.split(' ')[1]) + ' was added with phone number ' + str(add_string.split(' ')[2])


@input_error
def handler_changer(change_string: str):
    if str(change_string.split(' ')[1]).isdigit() or str(change_string.split(' ')[1]) == '':
        return "Incorrect user name. Try again"
    if not str(change_string.split(' ')[2]).isdigit() or str(change_string.split(' ')[2]).isdigit() == '':
        return "Incorrect phone number. Try again"
    MY_PHONEBOOK[str(change_string.split(' ')[1])] = str(change_string.split(' ')[2])
    return 'The phone number for contact ' + str(change_string.split(' ')[1]) + ' was changed'


@input_error
def handler_phone_show(phone_show_string: str):
    return 'The phone number for ' + str(phone_show_string.split(' ')[1]) + ' is ' \
           + MY_PHONEBOOK[str(phone_show_string.split(' ')[1])]


def main():
    while True:
        tmp = input('Please input command: ')
        if tmp.lower() == 'good bye' or tmp.lower() == 'close' or tmp.lower() == 'exit':
            print("Good bye!")
            break
        elif tmp.lower() == 'hello':
            print('How can I help you?')
        elif tmp.lower() == 'show all':
            print(MY_PHONEBOOK)
        elif tmp.lower().split(' ')[0] == 'add':
            handler_adder(tmp)
        elif tmp.lower().split(' ')[0] == 'change':
            handler_changer(tmp)
        elif tmp.lower().split(' ')[0] == 'phone':
            handler_phone_show(tmp)
        else:
            print('There is no such a command. Please try again')


if '__main__' == __name__:
    main()
