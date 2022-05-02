"""
Напишите функцию real_len, которая подсчитывает и возвращает длину строки
без следующих управляющих символов: [\n, \f, \r, \t, \v]
Для проверки правильности работы функции real_len ей будут переданы следующие строки:

'Alex\nKdfe23\t\f\v.\r'
'Al\nKdfe23\t\v.\r'
"""


def real_len(text):
    real_str_len = 0
    for i in text:
        if i == '\n' or i == '\f' or i == '\r' or i == '\t' or i == '\v':
            continue
        else:
            real_str_len += 1
    return real_str_len

def main():
    string = 'Alex\nKdfe23\t\f\v.\r'
    
    print(real_len(string))
   

if __name__ == '__main__':
    main()