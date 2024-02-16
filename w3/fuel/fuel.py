def main():
    while True:
        inp = input('Fraction: ')
        try:
            X,Y = inp.split('/')
            X,Y = int(X), int(Y)
            res = (X/Y)*100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if X>Y:
                continue
            if res <=1:
                print('E')
            elif res>= 99:
                print('F')
            else:
                print(str(round(res))+'%')
            break

if __name__ == '__main__':
    main()
