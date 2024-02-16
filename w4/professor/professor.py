import random

def main():
    score= 0
    level = get_level()
    for _ in range(0,10):
        X,Y = generate_integer(level), generate_integer(level)
        tries= 1
        while True:
            try:
                ans= int(input(f'{X} + {Y} ='))
                if ans==X+Y:
                    score+=1
                    break
                if tries==3:
                    print(f'{X} + {Y} = {X+Y}')
                    break
                else:
                    tries+=1
                    print('EEE')
                    continue
            except ValueError:
                tries+=1
                continue
    print(f'Score:{score}')


def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)
        case _:
            pass



if __name__ == "__main__":
    main()
