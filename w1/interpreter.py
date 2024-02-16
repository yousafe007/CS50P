a, o, b = input('Expression: ').split(' ')
a = int(a)
b = int(b)
match o:
    case '+':
        print(float(a+b))
    case '-':
        print(float(a-b))
    case '/':
        print(a/b)
    case '*':
        print(float(a*b))

