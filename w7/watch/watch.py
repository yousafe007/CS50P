import re
import sys


def main():
    print(parse(input("HTML: ")))

# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

def parse(s):
    if (matches := re.search(r"^<iframe.*https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)", s, re.IGNORECASE)):
        return f'https://youtu.be/{matches.group(1)}'
    else:
        return None



if __name__ == "__main__":
    main()
