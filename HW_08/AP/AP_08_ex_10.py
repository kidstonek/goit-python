"""
FIFO
(англ. first in, first out — «первым пришёл — первым ушёл») — способ организации данных или другими словами очередь.
Это выражение описывает принцип технической обработки очереди или обслуживания конфликтных требований путём упорядочения
процесса по принципу: «первым пришёл — первым обслужен» (ПППО). Тот, кто приходит первым, тот и обслуживается первым,
пришедший следующим ждёт, пока обслуживание первого не будет закончено, и так далее.

С помощью коллекции deque реализуйте структуру данных FIFO. Создайте переменную fifo, содержащую коллекцию deque.
Ограничьте ее размер с помощью константы MAX_LEN. Функция push добавляет значение element в конец списка fifo.
Функция pop достает и возвращает первое значение из списка fifo.
"""

from collections import deque

MAX_LEN = 10

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():

    return fifo.popleft()


def main():
    push('WU')
    push('Tang')
    push('Clan')
    print(fifo)
    pop()
    print(fifo)

    ...

# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
