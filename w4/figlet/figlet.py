import sys
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    random = False
    if len(sys.argv) ==0:
        random = True
    if len(sys.argv)==3:
        if(sys.argv[1] not in ['-f', '--font']) or sys.argv[2] not in fonts:
           print('Invalid usage')
           sys.exit(1)
    else:
        sys.exit(1)
    st = input('Input: ')

    if not random:
        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
            print('Output:\n', figlet.renderText(st))
    else:
        figlet.setFont(font=random.choice(fonts))





if __name__ == '__main__':
    main()
