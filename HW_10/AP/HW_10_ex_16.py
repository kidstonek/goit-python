"""
Завершаем функциональность класса Contacts. На этом этапе мы добавим в класс метод remove_contacts.
Метод должен удалять контакт по уникальному id в списке contacts. Если словаря с указанным
id в списке contacts не найдено, метод никаких действий над списком contacts не производит.

Примечание: для правильного прохождения теста не создавайте экземпляр класса в коде.

"""


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.contacts.append(
            {
                "id": Contacts.current_id,
                "name": name,
                "phone": phone,
                "email": email,
                "favorite": favorite,
            }
        )
        Contacts.current_id += 1

    def get_contact_by_id(self, id):
        result = list(filter(lambda contact: contact.get("id") == id, self.contacts))
        return result[0] if len(result) > 0 else None

    def remove_contacts(self, id):
        result = list(filter(lambda contact: contact.get("id") != id, self.contacts))
        self.contacts = result


def main():
    contact = Contacts()
    contact.add_contacts('Wylie Pope', '(692) 802-2949', 'est@utquamvel.net', True)
    contact.add_contacts('Cyrus Jackson', '(501) 472-5218', 'nibh@semsempererat.com', False)
    contact.add_contacts('A', '(501) 472-5218', 'nibh@semsempererat.com', False)
    print(contact.list_contacts())
    print(contact.remove_contacts(2))
    print(contact.list_contacts())


if '__main__' == __name__:
    main()
