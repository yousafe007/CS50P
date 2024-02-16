sum= 0
due = 50
while sum < 50:
    print('Amount Due: ' + str(due))
    inp = int(input('Insert Coin: '))
    if(inp not in [25, 10, 5]):
        continue
    sum+=inp
    due-= inp
print('Change Owed: ' +str(abs(due)))
