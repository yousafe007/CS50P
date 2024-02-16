import sys
import os.path

def main():

    if not correct_args_num():
        sys.exit('Enter only one command line argument!')

    file_name = sys.argv[1]

    if not file_exists(file_name):
        sys.exit('File does not exist')

    if not is_python_file(file_name):
        sys.exit("Not a '.py' file!")

    print(count_lines(file_name))

def correct_args_num():
    if len(sys.argv) == 2:
        return True


def is_python_file(string: str):
    return string.endswith('.py')

def file_exists(file: str):
    return os.path.isfile(file)

def is_comment(line:str):
    return line.startswith('#')

def count_lines(f):
    count = 0
    with open(f) as file:
        lines = [line for line in file.readlines() if line.strip()]

    for line in lines:
        if not is_comment(line.lstrip()):
            count+=1
    return count

if __name__ == '__main__':
    main()
