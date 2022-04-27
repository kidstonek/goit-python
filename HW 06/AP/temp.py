

"""
strr = 'Nikita Borisenko,2000'

tmp_dig = ''
answer = 0

tmp_dig = strr[strr.find(',')+1:]
for i in strr:
    if i in '1234567890':
        #print('ok')
        tmp_dig = tmp_dig + i

#answer = answer + int(tmp_dig)
print(tmp_dig)    """

emp_list = [['Robert Stivenson,28', 'Alex Denver,30'],['Drake Mikelsson,19']]

for i in emp_list:
    #if type(i) == list:
        for k in i:
            print(k)
        