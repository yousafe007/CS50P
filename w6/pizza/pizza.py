import sys
import os.path
import csv
from tabulate import tabulate

def main():

    if not correct_args_num():
        sys.exit('Enter only one command line argument!')

    file_name = sys.argv[1]

    if not file_exists(file_name):
        sys.exit('File does not exist')

    if not is_csv_file(file_name):
        sys.exit("Not a CSV file!")

    items = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        for row in csv_reader:
            items.append(row)
    print(tabulate(items, headers= header, tablefmt="grid"))

    '''
        Same solution with DictReader:

    items = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        # Convert each row (dict) into a list of values preserving the order of headers
        headers = csv_reader.fieldnames
        for row in csv_reader:
            # Append the values of each row, ensuring they match the header's order
            items.append(list(row.values()))
    print(tabulate(items, headers=headers, tablefmt="grid"))
    '''

def correct_args_num():
    if len(sys.argv) == 2:
        return True


def is_csv_file(string: str):
    return string.endswith('.csv')

def file_exists(file: str):
    return os.path.isfile(file)

if __name__ == '__main__':
    main()
