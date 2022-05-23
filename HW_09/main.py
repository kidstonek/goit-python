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


Доволі складно читається Ваш декоратор, Ви туди вписали також і парсер даних. Винесіть цей код в іншу функцію.
Також обробку команл варто зробити в зовнішній функції, тоді і блок `main` - буде краще читатись)
"""

MY_PHONEBOOK = {}


def input_error(in_func):
    def wrapper(some_string):
        try:
            check = in_func(some_string)
            return check
        except KeyError:
            return 'There is no such a contact. Please try again'
        except IndexError:
            return 'Give me name and phone please'
        except ValueError:
            return 'ValueError'
        except TypeError:
            return 'TypeError'
    return wrapper


def handler_hello():
    return 'How can I help you?'


@input_error
def handler_adder(add_string: str):
    if not str(add_string.lower().split(' ')[0]) == 'add':
        return add_string
    MY_PHONEBOOK[str(add_string.split(' ')[1])] = str(add_string.split(' ')[2])
    return 'Contact ' + str(add_string.split(' ')[1]) + ' was added with phone number ' + str(add_string.split(' ')[2])


@input_error
def handler_changer(change_string: str):
    if not str(change_string.lower().split(' ')[0]) == 'change':
        return change_string
    MY_PHONEBOOK[str(change_string.split(' ')[1])] = str(change_string.split(' ')[2])
    return 'The phone number for contact ' + str(change_string.split(' ')[1]) + ' was changed'


@input_error
def handler_phone_show(phone_show_string: str):
    return 'The phone number for ' + str(phone_show_string.split(' ')[1]) + ' is ' \
           + MY_PHONEBOOK[str(phone_show_string.split(' ')[1])]


@input_error
def command_checker(command_string: str):
    if str(command_string.lower().split(' ')[0]) == 'add':
        tmp = str(command_string.split(' ')[1])
        for i in filter(lambda x: bool(x == tmp), MY_PHONEBOOK.keys()):
            return "Such a name already exists. Please try again"
    if str(command_string.lower().split(' ')[1]).isdigit() or str(command_string.lower().split(' ')[1]) == '':
        return "Incorrect user name. Try again"
    if str(command_string.lower().split(' ')[0]) == 'phone':
        return command_string
    if not str(command_string.split(' ')[2]).isdigit() or str(command_string.split(' ')[2]).isdigit() == '':
        return "Incorrect phone number. Try again"
    else:
        return command_string


USERS_COMMANDS = {handler_hello: 'hello', handler_phone_show: 'phone', handler_changer: 'change', handler_adder: 'add'}


def main():
    while True:
        tmp = input('Please input command: ')
        if tmp.lower() == 'good bye' or tmp.lower() == 'close' or tmp.lower() == 'exit':
            print("Good bye!")
            break
        if tmp.lower() == 'show all':
            print(MY_PHONEBOOK)
        for k, v in USERS_COMMANDS.items():
            if v == tmp.lower().split(' ')[0]:
                print(k(command_checker(tmp)))


if '__main__' == __name__:
    main()
