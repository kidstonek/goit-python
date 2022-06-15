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
    def __init__(self, name: Name, phone=None):
        self.name = name
        self.phone = phone

    def add_number_to_record(self, *args):
        # for i in range(len(args[1:])):
        #     self.phone.value.append(args[i])
        #     print(args[i])
        return self.phone.value.append[args]

    def del_number_from_record(self, name: Name, *args):
        pass

    def change_number_in_record(self, name: Name, *args):
        pass


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_to_addressbook(self, name: Name, record: Record):
        self.data[name.value] = record


def ex(*args):
    return "Good bye!"


@input_error
def add_to_addressbook(addressbook: AddressBook, *args):
    print(args)
    if args[0].isdigit():
        return "The contact name should be in letters"
    tmp_name = Name(args[0])
    tmp_phone1 = Phone(list(args[1:]))
    tmp_rec = Record(tmp_name, tmp_phone1)
    addressbook.add_to_addressbook(tmp_name, tmp_rec)
    return f'Contact {tmp_rec.name.value} with phones {tmp_phone1.value} added successfully'


@input_error
def show_addressbook(addressbook: AddressBook, *args):
    for k, v in addressbook.data.items():
        print(k, v.phone.value)


@input_error
def find_contact(addressbook: AddressBook, *args):
    for k, v in addressbook.data.items():
        if k == args[0]:
            return k, v.phone.value


@input_error
def add_phone_to_contact(addressbook: AddressBook, *args):
    for k, v in addressbook.data.items():
        if k == args[0]:
            return Record.add_number_to_record(addressbook.data.get(args[0]), list(args[1:]))


COMMANDS = {ex: ["exit", ".", "bye"], show_addressbook: ["show", "s"], add_to_addressbook: ["add"],
            find_contact: ["find", "f"], add_phone_to_contact: ["ap"]}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")


def main():
    phone_book = AddressBook()
    name1 = Name('Alberto')
    name2 = Name('Dell')
    name3 = Name('Rio')

    phone1 = Phone('+3232323')
    phone2 = Phone('+6666664')
    phone3 = Phone('+23432423')

    r = Record(name1, phone1)
    r2 = Record(name2, phone2)
    r3 = Record(name3, phone3)
    print(r3)
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
