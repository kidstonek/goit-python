"""
Есть список contacts, элементы которого — словари контактов следующего вида:
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    }

Словарь содержит имя пользователя, его email, телефонный номер и свойство — избранный контакт или нет.

Создайте функцию get_favorites(contacts), которая будет возвращать список, содержащий только избранные контакты.
Используйте при этом функцию filter, чтобы отфильтровать по полю favorite только избранные контакты.
"""


def get_favorites(contacts):
    fav_contacts = []
    for i in filter(lambda x: bool(x.get('favorite')), contacts):
        fav_contacts.append(i)
    return fav_contacts


def main():
    fav_list = [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
                {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False},
                {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': True},
                {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False},
                {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': True}]
    print(get_favorites(fav_list))


if '__main__' == __name__:
    main()
