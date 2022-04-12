from os import access
from re import S
from unittest import result

'''
is_active = bool(input("Пользователь активен? "))
is_admin = bool(input("Пользователь администратор? "))
is_permission = bool(input("Пользователь имеет доступ? "))

access = (is_active and is_permission) or is_admin

print(access)




if is_admin:
    print('user is admin')
else:
    if is_active and is_permission:
        print('user is just user')
#print (is_active, is_admin, is_permission)


num = int(input("Введите целое число: "))

is_even = 'True' if num % 2 == 0 else 'False'

print(is_even)

fruit = 'apple'
for cr in fruit:
    print(cr)

# 0 + 1 + 2 + 3 + 4 + 5
num = int(input("Введите целое число (0 до 100): "))
sum = 0
i = 1 
while i <= num:
    sum = sum + i
    i += 1
  

print(sum)

#########
count = 0
message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
for cr in message:
    if cr == 'e':
        count += 1
    
print(count)


##################################
first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
if first < second:
    nod = first
else:
    nod = second
while True:
    if (first % nod == 0) and (second % nod == 0):
        break
    nod = nod - 1 
###################################################
Переменная nod имеет неправильное значение, 
0 должно быть: nod=25 first=375 second=575
################################################
Расччет суммы елементов в листе
num = int(input("Введите целое число : "))
sum = 0
for i in range(num+1):
    sum = sum + i
    
print(sum)
##############################################

HW2ex10
num = int(input("Введите целое число (0 для выхода): "))
sum = 0

while num != 0:
    
    for i in range(num+1):
        
        sum = sum + i
        #print(sum)
    num = int(input("Введите целое число (0 для выхода): "))
print(sum)



## HW2ex11
sum = 0
while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    
    for i in range(num + 1):
        sum = sum + i
print(sum)


## HW2ex12
Вернемся снова к нашей предыдущей задаче.

Напишите два двойных цикла. В первом цикле while мы постоянно запрашиваем целое число, 
а во втором с помощью цикла for считаем сумму четных чисел от 0 до введенного числа. 
Выход из первого цикла осуществляем, если ввели число 0, с помощью оператора break.

Тесты используют две тестовые последовательности чисел:

10, 13, 73, 0 и ожидают сумму 1404
1, 2, 3, 4, 0 и ожидают сумму 10

sum = 0
while True:
    num = int(input("Введите целое число (0 для выхода): "))
    if num == 0:
        break
    for i in range(num + 1):
        if i % 2 != 0:
            continue
        sum = sum + i
print(sum)

###########################
### Задача: код Цезаря
A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z.

message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if (ch == ' ') or (ch == '!'):
        encoded_message = encoded_message + ch
        continue
    if ord(ch) >= 97:
        pos = abs(ord(ch) - ord('a'))
        pos = abs((pos + offset) % 26)
        encoded_message = encoded_message + chr(pos + ord("a"))
    else:
        pos = abs(ord(ch) - ord('A'))
        pos = abs((pos + offset) % 26)
        encoded_message = encoded_message + chr(pos + ord("A"))
    
    #encoded_message = encoded_message + chr(pos + ord("A"))
print(encoded_message)
##########################
HW2ex15
'''

result = None
operand = None
operator = None
wait_for_number = True

while True:
    tmp = input('введи что-то ,мудила: ')
    if tmp == '=':
        print(result)
        break

    if wait_for_number == True:
        if (tmp == '+') or (tmp == '-') or (tmp == '/') or (tmp == '*'):
            print(f"{tmp} is not a number. Try again.")
            continue
        else:
            if result == None:
                result = float(tmp)
            operand = float(tmp)
            wait_for_number = False

    elif wait_for_number != True:
        """
        if (tmp != "+") or (tmp != "-") or (tmp != "*") or (tmp != "/"):
            print(f"{tmp} is not '+' or '-' or '/' or '*'. Try again")
            continue
        """
        if tmp == "+":
            result += operand
            wait_for_number = True
            print("Mi tut")
        if tmp == "-":
            result = result - operand
            wait_for_number = True
        if tmp == "*":
            result = result * operand
            wait_for_number = True
        if tmp == "/":
            result = result / operand
            wait_for_number = True


'''
    if wait_for_number:
        if (tmp == '+') or (tmp == '-') or (tmp == '/') or (tmp == '*'):
            print(f"{tmp} is not a number. Try again.")
            continue
    operand = tmp
    print(operand)
    wait_for_number = False
    
        
    
    
    if wait_for_number == False:
        if (tmp != '+') or (tmp != '-') or (tmp != '/') or (tmp != '*'):
            print(f"{tmp} is not '+' or '-' or '/' or '*'. Try again")
            continue
    operator = tmp
    print(operator)'''



#print(operator, operand)

'''
    if wait_for_number:
        if (tmp == '+') or (tmp == '-') or (tmp == '/') or (tmp == '*'):
            print("Алеша, шо ты делаешь!!!")
            operand = tmp
            continue
        
        
    else:
        operator = tmp
'''