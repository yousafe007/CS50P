import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    #var 1: 9:00 AM to 5:00 PM
    #var 2: 9 AM to 5 PM


    variant = -1
    if (matches := re.search(r"^([1]?[0-9]):?([0-5]+[0-9])?\s+(AM|PM)\s+to\s+([1]?[0-9]):?([0-5]+[0-9])?\s+(AM|PM)$", s, re.IGNORECASE)):
        von, mins1, period1, bis, mins2, period2 = matches.groups()
    else:
        raise ValueError

    if mins1 == mins2 == None:
        variant = 2
    else:
        variant = 1

    if period1=='PM' and von != '12':
        von = str((int(von)+12)%24)
    elif period1=='AM' and von == '12':
        von = '00'
    if period2=='PM'and bis != '12':
        bis = str((int(bis)+12)%24)
    elif period2=='AM' and bis == '12':
        bis = '00'

    if variant==1:

        return f'{von.zfill(2)}:{mins1} to {bis.zfill(2)}:{mins2}'
    else:
        return f'{von.zfill(2)}:00 to {bis.zfill(2)}:00'




if __name__ == "__main__":
    main()
