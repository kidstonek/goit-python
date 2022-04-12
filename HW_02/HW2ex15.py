import re


result = None
operand = None
operator = None
wait_for_number = True

while True:
    tmp = input('введи что-то ,мудила: ')
    if wait_for_number == True:
        if tmp == '=':
            print(f'Result: ', result)
            break
        if (tmp == '-') or (tmp == '+') or (tmp == '/') or (tmp == '*'):
            print("ты ввел знак вместо числа!!! Попробуй еще раз")
            continue
        else:
            if  result == None:
                result = float(tmp)
                wait_for_number = False
                continue
            try:
                operand = float(tmp)
            except ValueError:
                continue

            if operator == '+':
                result = result + operand
                wait_for_number = False
                continue
            if operator == '-':
                result = result - operand
                wait_for_number = False
                continue
            if operator == '/':
                result = result / operand
                wait_for_number = False
                continue
            if operator == '*':
                result = result * operand
                wait_for_number = False
                continue

    if wait_for_number == False:

        if tmp == '=':
            print(f'Result: ', result)
            break
        if tmp == '+':
            operator = (tmp)
            #print(f'введен оператор{operator}')
            wait_for_number = True
            continue
        if tmp == '-':
            operator = (tmp)
            #print(f'введен оператор{operator}')
            wait_for_number = True
            continue
        if tmp == '/':
            operator = (tmp)
            #print(f'введен оператор{operator}')
            wait_for_number = True
            continue
        if tmp == '*':
            operator = (tmp)
            #print(f'введен оператор{operator}')
            wait_for_number = True
            continue
        else:
            print(f'{tmp} is not ''+'' or ''-'' or ''/'' or ''*''. Try again')
            continue
