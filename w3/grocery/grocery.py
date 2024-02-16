

def main():
    grocery_list = {}

    while True:
        try:
            inp = input().upper()
            if not inp:
                continue
            if inp in grocery_list:
                grocery_list[inp]+= 1
            else:
                grocery_list[inp]=1
        except EOFError:
            for k,v in sorted(grocery_list.items()):
                print(f'{v} {k}')
            break


if __name__ == '__main__':
    main()
