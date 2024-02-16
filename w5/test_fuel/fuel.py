def main():
    while True:
        try:
            inp = input('Fraction: ')
            inp = convert(inp)
        except (ValueError, ZeroDivisionError):
            pass
        else:
           print(gauge(inp))
           break

def convert(inp):
        X,Y = inp.split('/')
        if not X.isdigit() or not Y.isdigit():
            raise ValueError

        X,Y = int(X), int(Y)
        if Y==0:
            raise ZeroDivisionError
        if X>Y:
            raise ValueError

        return (X/Y)*100

def gauge(percentage):
    if percentage <=1:
        return 'E'
    elif percentage>= 99:
        return 'F'
    else:
        return str(round(percentage))+'%'



if __name__ == "__main__":
    main()

