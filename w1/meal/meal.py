def main():
    inp = input('What time is it? ')
    inp = convert(inp)

    if 7<=inp <=8:
        print('breakfast time')
    elif 12<=inp<=13:
        print('lunch time')
    elif 18<=inp<=19:
        print('dinner time')
    else:
        pass


def convert(time):
    hours, minutes = time.split(":")
    return float(hours)+(float(minutes)/60)


if __name__ == "__main__":
    main()
