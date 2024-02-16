from datetime import date
import sys
import inflect

def main():
    if (mins := to_minutes(input('Date of Birth: '))):
        print(f'{mins.capitalize()} minutes')
    else:
        sys.exit('Invalid date')

def to_minutes(string):
    try:
        y,m,d = parse_date(string)
        d_obj = date(y,m,d)
        delta_days = date.today()-d_obj
        if delta_days.days < 0:  # Check if the date is in the future
            return None
        return num_to_word(delta_days.days*24*60)
    except ValueError:
        return None

def parse_date(date_str):
    year, month, day = map(int, date_str.split('-'))
    return (year, month, day)

def num_to_word(int):
  p = inflect.engine()
  return p.number_to_words(int, andword="")



if __name__ == "__main__":
    main()
