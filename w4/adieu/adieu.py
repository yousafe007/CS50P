import inflect

def main():
    p = inflect.engine()
    names = []
    try:
        while True:
            name = input('Name: ')
            names.append(name)
    except EOFError:
        print('Adieu, adieu, to ' +p.join(names,sep=','))

if __name__ == '__main__':
    main()
