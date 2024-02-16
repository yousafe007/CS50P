import sys
import requests
import json



def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')
    if not isfloat(sys.argv[1]):
        sys.exit('Not a float!')

    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        rate = r.json()['bpi']['USD']['rate'].replace(',','')
        print(f'${float(rate)*float(sys.argv[1]):,.4f}')
    except requests.RequestException:
        pass



def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    main()

