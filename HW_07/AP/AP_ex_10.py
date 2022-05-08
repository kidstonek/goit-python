"""
При работе веб-сервисов общение по протоколу HTTP чаще всего происходит в формате JSON.
И отправка данных на сервер при POST запросе — это необходимость использовать словарь, так как структура
формата JSON идентична словарю Python.

Реализуйте вспомогательную функцию, которая будет формировать запрос на сервер в виде словаря.
Данная функция make_request(keys, values) принимает два параметра в виде списков. Функция должна создать словарь с ключами
из списка keys и значениями из списка values.

Порядок соответствия совпадает с индексами списков keys и data.
Если длина keys и values не совпадают, верните пустой словарь.

"""
def make_request(keys:list, values:list):
    total_list = {}
    if len(keys) != len(values):
        return total_list
    for i in range(len(keys)):
        total_list[keys[i]] = values[i]
        
    return total_list



def main():
   input_list = {"key": "value", "new_key": "new value"}
   list_of_keys = ['rat', 'cat', 'dog']
   list_of_values = ['small', 'pretty', 'gav-gav']
   print(make_request(list_of_keys, list_of_values))


if __name__ == '__main__':
    main()

    