import sys
import os.path
import csv
def main():

    if not correct_args_num():
        sys.exit("Usage: script.py input.csv output.csv")

    file1 = sys.argv[1]
    file2 = sys.argv[2]

    if not file_exists(file1):
        sys.exit(f'Could not read {file1}')

    if not is_csv_file(file1) or not is_csv_file(file2):
        sys.exit("Not a CSV file!")
    with open(file1, mode='r') as input_file, open(file2, 'w', newline='') as output_file:
        csv_reader = csv.DictReader(input_file)
        headers = csv_reader.fieldnames

        w = csv.DictWriter(output_file, fieldnames=['first', 'last', 'house'])
        w.writeheader()

        for row in csv_reader:
            first, last = row[headers[0]].replace(' ', '').split(',')[::-1]
            w.writerow({'first':first, 'last': last, 'house':row[headers[1]]})

def correct_args_num():
    if len(sys.argv) == 3:
        return True

def is_csv_file(string: str):
    return string.endswith('.csv')

def file_exists(file: str):
    return os.path.isfile(file)

if __name__ == '__main__':
    main()
