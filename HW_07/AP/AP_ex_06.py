"""
Реализуйте функцию solve_riddle(riddle, word_length, start_letter, reverse=False) для нахождения искомого слова в строке ребуса.

Параметры функции:

riddle - строка с зашифрованным словом.
word_length - длина зашифрованного слова.
start_letter - буква, с которой начинается слово (подразумевается, что до начала слова буква не встречается в строке).
reverse - указывает, в каком порядке записано слово. По умолчанию — в прямом. Для значения True слово зашифровано
в обратном порядке, к примеру, в строке mi1rewopret зашифровано слово power.
Функция должна возвращать первое найденное искомое слово. Если слово не найдено, вернуть пустую строку.
"""
def solve_riddle(riddle, word_length, start_letter, reverse=False):
    if reverse == True:
        riddle = riddle[::-1]
    return riddle[riddle.find(start_letter):riddle.find(start_letter)+word_length]

def main():
    print(solve_riddle('mi1powerpret', 5, 'p'))

if __name__ == '__main__':
    main()