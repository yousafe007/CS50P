import random

def main():
    level = 0
    while True:
        level = input('Level: ')
        if level.isdigit():
            if int(level) >0:
                break
        else:
            continue
    level = int(level)
    random_int = random.randint(1,level)

    while True:
        guess = input('Guess: ')
        if not guess.isnumeric():
            continue
        else:
            guess = int(guess)
        if guess< random_int:
            print('Too small!')
        elif guess > random_int:
            print('Too large!')
        else:
            print('Just right!')
            break



if __name__ == '__main__':
    main()
