v = input('camelCase: ')

new_v = v[0]
for i in v[1:]:
    if i.isupper():
        new_v += '_' + i
    else:
        new_v += i
print(new_v.lower(), end='')
