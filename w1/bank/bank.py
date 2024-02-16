input = input('Greeting: ').strip().lower()
if 'hello' in input:
    print('$0')
elif input[0]=='h':
    print('$20')
else:
    print('$100')
