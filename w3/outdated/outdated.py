def main():
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        inp = input('Date: ')
        try:
            # Try to parse the date assuming it's in MM/DD/YYYY format.
            m, d, y = map(int, inp.split('/'))
            if not month_in_range(m) or not day_in_range(d):
                continue
            print(f'{y}-{m:02d}-{d:02d}')
            break
        except ValueError:
            try:
                # Parse the date assuming it's in "Month DD, YYYY" format.
                m_d, y = inp.split(', ')
                m, d = m_d.split(' ')

                if m in month_list:
                    m = month_list.index(m) + 1  # Convert month name to number
                    d, y = int(d), int(y)  # Convert day and year to integers
                    if not month_in_range(m) or not day_in_range(d):
                        continue
                    print(f'{y}-{m:02d}-{d:02d}')
                    break
                else:
                    print("Invalid month name.")
            except ValueError:
                # If input does not match either format, inform the user.
                print("Invalid date format. Please enter the date in MM/DD/YYYY or Month DD, YYYY format.")

def month_in_range(m):
    return 0<m<13
def day_in_range(d):
    return 0<d<32

if __name__ == '__main__':
    main()
mkdir emojize
