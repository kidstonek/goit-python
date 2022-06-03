from collections import UserDict


class Field:
    pass


class Phone(Field):
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        self.value = value


class Record:
    def __init__(self):
        self.phone = None
        self.name = None

    def add_record(self, name: Name, phone=None):
        self.name = name
        self.phone = phone


class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_to_addressbook(self, name: Name, record: Record):
        self.data[name.value] = record


def ex(*args):
    return "Good bye!"


COMMANDS = {ex: ["exit", ".", "bye"]}


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

    r = Record()
    r2 = Record()
    r3 = Record()

    r.add_record(name1, phone1)
    r2.add_record(name2, phone2)
    r3.add_record(name3, phone3)
    phone_book.add_to_addressbook(name1, r)
    phone_book.add_to_addressbook(name2, r2)
    phone_book.add_to_addressbook(name3, r3)
    print(phone_book)

    # while True:
    #     tmp = input('Please input command: ')
    #     result, data = parse_command(tmp)
    #     print(result(phone_book, *data))
    #     if result is ex:
    #         break


if '__main__' == __name__:
    main()