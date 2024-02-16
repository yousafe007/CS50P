def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    total = 0
    while True:
        try:
            inp = input('Input: ').title()
            if inp.title() in menu:
                total += menu[inp]
                print(f'Total: ${total:.2f}')
        except EOFError:
            print(f'Total: ${total:.2f}')
            break
        except KeyError:
            pass


if __name__ == '__main__':
    main()
