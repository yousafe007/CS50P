inp = input('Input: ')

newstr =''
for i in inp:
    if i.upper() not in ['A', 'E', 'I', 'O', 'U']:
        newstr +=i
print('Output: ' + newstr)
