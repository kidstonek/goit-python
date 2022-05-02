
"""
Вернемся к нашей задаче с телефонными номерами. Компания расширяется и вышла на рынок Азии. Теперь в списке приходят телефоны разных стран. Каждая страна имеет свой телефонный код.

Компания работает со следующими странами

Страна	Код ISO	Префикс

Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380

Чтобы мы могли корректно выполнить маркетинговую SMS кампанию, необходимо выдать для каждой страны свой список телефонных номеров.

Напишите функцию get_phone_numbers_for_сountries, которая будет:

1. Принимать список телефонных номеров.
2. Санитизировать (нормализовать) полученный список телефонов клиентов с помощью нашей функции sanitize_phone_number.
3. Сортировать телефонные номера по указанным в таблице странам.
4. Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:


{
    "UA" : [<здесь список телефонов>],
    "JP": [<здесь список телефонов>],
    "TW": [<здесь список телефонов>],
    "SG": [<здесь список телефонов>]
}

5. Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен в список словаря с ключом "UA".

Функция возвращает неправильное значение: {'UA': ['380998759405', '818765347', '8867658976', '657658976'], 'JP': [], 'SG': [], 'TW': []}. Должно быть: test_get_phone_numbers_for_countries(['380998759405', '818765347', '8867658976', '657658976']) == {'UA': ['380998759405'], 'JP': ['818765347'], 'TW': ['8867658976'], 'SG': ['657658976']}

"""






def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    
    return new_phone


def get_phone_numbers_for_countries(list_phones):
    list_phones_JP = []
    list_phones_TW = []
    list_phones_SG = []
    list_phones_UA = []
    total_numbers_dict = {}

    for phones in list_phones:
        
        if "81" in sanitize_phone_number(phones):
            list_phones_JP.append(sanitize_phone_number(phones)) 
        elif "886" in sanitize_phone_number(phones):
            list_phones_TW.append(sanitize_phone_number(phones))       
        elif "65" in sanitize_phone_number(phones)[0:2]:
            list_phones_SG.append(sanitize_phone_number(phones))
        else:
            list_phones_UA.append(sanitize_phone_number(phones))
    
    total_numbers_dict['UA'] = list_phones_UA
    total_numbers_dict['JP'] = list_phones_JP
    total_numbers_dict['SG'] = list_phones_SG
    total_numbers_dict['TW'] = list_phones_TW

    return total_numbers_dict

    ...


def main():
   """ list_phones_JP = []
    list_phones_TW = []
    list_phones_SG = []
    list_phones_UA = []
    test_dict = {}
    total_numbers_dict = {}"""

unsorted_numbers = ['065-875-94-11', '(81)8765347', '8867658976', '657658976', '(65)765-89-77']
"""for phones in unsorted_numbers:
        if "+81" in phones:
            list_phones_JP.append(sanitize_phone_number(phones))        
        elif "+65" in phones:
            list_phones_SG.append(sanitize_phone_number(phones))
        elif "+886" in phones:
            list_phones_TW.append(sanitize_phone_number(phones))
        elif "+380" in phones:
            list_phones_UA.append(sanitize_phone_number(phones))
        else:
            list_phones_UA.append(sanitize_phone_number(phones))"""
            

    #print(total_numbers_dict)

print(get_phone_numbers_for_countries(unsorted_numbers))
    

    

if __name__ == '__main__':
    main()