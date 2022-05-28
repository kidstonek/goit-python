"""
Реализуйте класс Contacts, который будет работать с контактами. На первом этапе мы добавим два метода.

list_contacts возвращает список контактов, переменная contacts из текущего экземпляра класса
add_contacts добавляет новый контакт в список, который является переменной объекта — contacts
Класс Contacts содержит переменную класса current_id. Мы будем использовать ее при добавлении нового контакта
в качестве уникального идентификатора контакта. Когда мы добавляем новый контакт, то передаем такие аргументы в
метод add_contacts: name, phone, email и favorite. Метод должен создать словарь с указанными ключами и значениями из
параметров функции. Также необходимо добавить в словарь новый ключ id,
значением которого является значение переменной класса current_id.

Пример полученного словаря:
    {
        "id": 1,
        "name": "Wylie Pope",
        "phone": "(692) 802-2949",
        "email": "est@utquamvel.net",
        "favorite": True,
    }
Указанный словарь мы добавляем в список contacts. Не забываем увеличивать переменную
current_id на единицу после каждого вызова метода add_contacts для сохранения уникальности ключа id для словаря.

Примечание: для правильного прохождения теста не создавайте экземпляр класса в коде.
"""


class Contacts:
    current_id = 1

    def __init__(self):
        self.contacts = []

    def list_contacts(self):
        return self.contacts

    def add_contacts(self, name, phone, email, favorite):
        self.name = name
        self.phone = phone
        self.email = email
        self.favorite = favorite
        self.contacts.append({'id': Contacts.current_id, 'name': self.name, 'phone': self.phone, 'email': self.email,
                              'favorite': self.favorite})
        Contacts.current_id += 1


def main():
    contact = Contacts()
    contact.add_contacts('Biba', 1232132, 'dasdad@dada434.ds', True)
    print(contact.list_contacts())


if '__main__' == __name__:
    main()