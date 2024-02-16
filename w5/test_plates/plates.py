
import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return  not period_space_punc(s) and max_5_min_2(s) and  two_letter(s) and mid_no(s)

def two_letter(s):
    return s[0].isalpha() and s[1].isalpha()

def max_5_min_2(s):
    return (2<=len(s)<=6)

def mid_no(s):
    is_num = False
    if not s[0].isalpha():
        return False
    for c in s[1:]:
        if not c.isalpha() and is_num == False:
            if c=='0':
                return False
            is_num = True
        elif c.isnumeric() and is_num == False:
            return False
        elif c.isalpha() and is_num == True:
            return False

    return True


def period_space_punc(s):
    for i in s:
        if i in (list(string.punctuation) +[' ']):
            return True
    return False


if __name__ == "__main__":
    main()
