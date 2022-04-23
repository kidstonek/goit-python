"""
Ваша компания проводит маркетинговые кампании с помощью SMS рассылок. 
Автоматический сбор телефонных номеров с базы данных формирует определенный список. Но клиенты оставляют свои номера в произвольном виде:

  "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",

Сервис рассылок прекрасно понимает и может отправить SMS-ку клиенту, только если телефонный номер содержит цифры. 
Необходимо реализовать функцию sanitize_phone_number, которая будет принимать строку с телефонным номером и нормализовать его, 
т.е. будет убирать символы (, -, ), + и пробелы.

Результат:

380501233234
0503451234
0508889900
380501112222
380501112211

"""
numbers_list = [
     "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def sanitize_phone_number(phone):
    correct_phone = ''
    for chr in phone:
        if chr.isdigit():
            correct_phone = correct_phone + chr
    return correct_phone

"""or 
    def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone"""





#============================
correct_phone = ''
test_number = "    +38(050)123-32-34"
for chr in test_number:
    if chr.isdigit():
        correct_phone = correct_phone + chr

print(correct_phone)