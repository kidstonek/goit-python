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
        except (KeyError, IndexError, ValueError, TypeError):
            return "Enter user name"
    return wrapper


def handler_adder(add_string: str):
    MY_PHONEBOOK[str(add_string.split(' ')[1])] = str(add_string.split(' ')[2])


def handler_changer(change_string: str):
    MY_PHONEBOOK[str(change_string.split(' ')[1])] = str(change_string.split(' ')[2])


def handler_phone_show(phone_show_string: str):
    return MY_PHONEBOOK[str(phone_show_string.split(' ')[1])]


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
            print(handler_phone_show(tmp))
        else:
            print('There is no such a command. Please try again')


if '__main__' == __name__:
    main()
