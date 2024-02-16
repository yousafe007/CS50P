def main():
    test_string = "Example String With Vowels"
    print(shorten(test_string))

def shorten(s):
    newstr = ''
    for i in s:
        if i not in 'AEIOUaeiou':
            newstr += i
    return newstr

if __name__ == "__main__":
    main()
