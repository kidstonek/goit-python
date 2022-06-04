from collections import UserDict


def input_error(in_func):
    def wrapper(*args):
        try:
            check = in_func(*args)
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


class Field:
    pass


class Phone(Field):
    def __init__(self, phone_list):
        self.value = phone_list


class Name(Field):
    def __init__(self, value):
        self.value = value


# Record реализует методы для добавления/удаления/редактирования объектов Phone.


class Record:
    def __init__(self, name: Name, *args):
        self.name = name
        self.phone = []
        if args:
            for i in range(len(args)):
                self.phone.append(args[i])

    def add_number_to_record(self, phone: Phone):
        self.phone.append(phone)

    def del_number_from_record(self, phone: Phone):
        # print(type(self.phone)) erase Rio +23432423
        for i in self.phone:
            if i.value == phone.value:
                self.phone.remove(i)

    def change_number_in_record(self, phone: Phone, phone_new: Phone):
        for i in self.phone:
            if i.value == phone.value:
                self.phone[self.phone.index(i)] = phone_new


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_to_addressbook(self, name: Name, record: Record):
        self.data[name.value] = record


def ex(*args):
    return "Good bye!"


# превращаю список телефонов в кортеж обьектов Phone
@input_error
def parse_phones(raw__p: list):
    tmp_p_list = []
    for i in raw__p:
        tmp_p = Phone(i)
        tmp_p_list.append(tmp_p)
    return tuple(tmp_p_list)


@input_error
def add_to_addressbook(addressbook: AddressBook, *args):
    if args[0].isdigit():
        return "The contact name should be in letters"
    tmp_name = Name(args[0])
    tmp_phone1 = parse_phones(list(args[1:]))
    tmp_rec = Record(tmp_name, tmp_phone1)
    addressbook.add_to_addressbook(tmp_name, tmp_rec)
    return f'Contact {tmp_rec.name.value} with phones {tmp_phone1} added successfully'


@input_error
def show_addressbook(addressbook: AddressBook, *args):
    showing_phone_book = {}
    for k, v in addressbook.data.items():
        phones = ', '.join([str(i.value) for i in v.phone])
        showing_phone_book[k] = phones
    return showing_phone_book

@input_error
def find_contact(addressbook: AddressBook, *args):
    for k, v in addressbook.data.items():
        if k == args[0]:
            return k, v.phone


@input_error
def add_phone_to_contact(addressbook: AddressBook, *args):
    for k, v in addressbook.data.items():
        if k == args[0]:
            add_num = Phone(args[1])
            Record.add_number_to_record(v, add_num)
            return f'Number {add_num.value} was added'


@input_error
def erase_phone(addressbook: AddressBook, *args):
    for k, v in addressbook.data.items():
        if k == args[0]:
            del_num = Phone(args[1])
            Record.del_number_from_record(v, del_num)
            return f'Number {del_num.value} was deleted'


def change_phone(addressbook: AddressBook, *args):
    for k, v in addressbook.data.items():
        if k == args[0]:
            ch_num_in = Phone(args[1])
            ch_num_for = Phone(args[2])
            Record.change_number_in_record(v, ch_num_in, ch_num_for)
            return f'Number {ch_num_in.value} was changed to {ch_num_for.value}'


COMMANDS = {ex: ["exit", ".", "bye"], show_addressbook: ["show", "s"], add_to_addressbook: ["add"],
            find_contact: ["find", "f"], add_phone_to_contact: ["ap"], erase_phone: ["erase"],
            change_phone: ["change", "ch"]}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")


def main():
    print('Welcome to the worst PhoneBook EVER')
    print('You can use following commands:')
    print('"show", "s" - to show the whole PhoneBook')
    print('"add" - to add the contact to the Phone book \\ example: add ContactName Phone \\+ Phone....')
    print('"ap" - add phone for existing contact \\ example: ap NameOfExistingContact Phone \\+ Phone....')
    print('"change", "ch" - to update existing phone number for contact \\ example: change '
          'NameOfExistingContact Phone \\+ Phone....')
    print('"erase" - to erase existing phone for the contact \\ example: erase NameOfExistingContact '
          'Phone \\+ Phone....')
    print('"exit", ".", "bye" - for exit')
    phone_book = AddressBook()
    name1 = Name('Alberto')
    name2 = Name('Dell')
    name3 = Name('Rio')

    phone1 = Phone('+3232323')
    phone2 = Phone('+6666664')
    phone3 = Phone('+23432423')

    r = Record(name1, phone1, phone3)
    r2 = Record(name2, phone2)
    r3 = Record(name3, phone3, phone2)

    phone_book.add_to_addressbook(name1, r)
    phone_book.add_to_addressbook(name2, r2)
    phone_book.add_to_addressbook(name3, r3)

    while True:
        tmp = input('Please input command: ')
        result, data = parse_command(tmp)
        print(result(phone_book, *data))
        if result is ex:
            break


if '__main__' == __name__:
    main()
