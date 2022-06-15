"""
Вам нужно реализовать полезную функцию для вывода списка коллег, которых надо поздравить с днём рождения на неделе.

У вас есть список словарей users, каждый словарь в нём обязательно имеет ключи name и birthday.
Такая структура представляет модель списка пользователей с их именами и днями рождения. name — это строка с именем
пользователя, а birthday — это datetime объект, в котором записан день рождения.

Ваша задача написать функцию get_birthdays_per_week, которая получает на вход список users и выводит в консоль
(при помощи print) список пользователей, которых надо поздравить по дням.
"""
import datetime
from datetime import datetime

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

birthdays_list = [
    {
        "name": "Valera", "birthday": "1997-05-16"
    },
    {
        "name": "Toha", "birthday": "1995-05-10"
    },
    {
        "name": "Billy", "birthday": "2001-05-22"
    },
    {
        "name": "Britany", "birthday": "1986-05-22"
    },
    {
        "name": "Britany", "birthday": "1986-05-11"
    },
    {
        "name": "Britany", "birthday": "1986-05-11"
    },
    {
        "name": "James", "birthday": "1979-05-16"
    },
    {
        "name": "Olga", "birthday": "2002-05-17"
    },
    {
        "name": "Helga", "birthday": "2002-05-17"
    },
    {
        "name": "Tetiana", "birthday": "1999-05-20"
    },
    {
        "name": "Vika", "birthday": "1990-05-18"
    },
]


def sort_week(week_dict: dict):  # сортируем список по дням недели
    sorted_dict = {}
    weekends_guys = ''
    week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    for day in week:
        for days_k, names_v in week_dict.items():
            if day == days_k:
                if days_k == 'Saturday' or days_k == 'Sunday':
                    weekends_guys = weekends_guys + ' ' + names_v.replace(' ', ', ')
                    continue
                sorted_dict[day] = names_v.replace(' ', ', ')
            if weekends_guys != '':
                sorted_dict['next Monday'] = weekends_guys.lstrip()
    return print_answer(sorted_dict)


def needed_month(colleagues_list):  # коллеги с датами у которых день рождения +7 дней от сегодня
    answer_list = []
    current_datetime = datetime.now()
    for elementy in colleagues_list:
        for k, v in elementy.items():
            if k == 'name':
                tmp_name = v
            if k == 'birthday':
                tmp = v.split('-')
                if (int(tmp[1]) == int(current_datetime.month)) and (int(tmp[2]) in range(current_datetime.day,
                                                                                          current_datetime.day + 7)):
                    answer_list.append({tmp_name: v})
    return answer_list


def print_answer(answer_dict: dict):   #печать ответа
    for k, v in answer_dict.items():
        print(k+':', v)


def all_b_days_in_week(birthday_dict): # список всех у кого ДР на неделе по дням
    tmp_dict = {}
    for i in birthday_dict:
        tmp_b_day = ''
        day_of_week = ' '.join(map(str, list(i.keys())))
        for ii in birthday_dict:
            if ii.keys() == i.keys():
                tmp = ''.join(map(str, list(ii.values())))
                tmp_b_day = tmp_b_day + ' ' + tmp
        for b in birthday_dict:
            if day_of_week in b:
                b.pop(day_of_week)
        if day_of_week == '':
            continue
        tmp_dict[day_of_week] = tmp_b_day.lstrip()
    return sort_week(tmp_dict)


def get_birthdays_per_week(colleagues_b_days): # коллеги у кого ДР на єтой неделе
    party_days = []
    current_datetime = datetime.now()
    lucky_people = needed_month(colleagues_b_days)
    for peoples in lucky_people:
        for names_p, b_dates_p in peoples.items():
            tmp_date = b_dates_p.split('-')
            tmp_date_day = datetime(year=int(current_datetime.year), month=int(current_datetime.month),
                                    day=int(tmp_date[2]))
            party_days.append({days_name[tmp_date_day.weekday()]: names_p})

    return all_b_days_in_week(party_days)


def main():
    get_birthdays_per_week(birthdays_list)


if __name__ == '__main__':
    main()


