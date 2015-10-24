def check_leap_year(year):
    if year and year.isdigit():
        int_year = int(year)
        if int_year % 4 == 0:
            if not(int_year % 100 == 0):
                print "%d is a leap year" % int_year
            else:
                if int_year % 400 == 0:
                    print "%d is a leap year" % int_year
                else:
                    print "%d is not a leap year" % int_year
        else:
            print "%d is not a leap year" % int_year

def is_leap_year(year):
    if year and year.isdigit():
        int_year = int(year)
        if int_year % 100 == 0:
            return int_year % 400 == 0
        return int_year % 4 == 0

def main():
    input_year=raw_input("What year: ")
    check_leap_year(input_year)
    leap_year = is_leap_year(input_year)
    if leap_year:
        print "%s is a leap year" % input_year
    else:
        print "%s is not a leap year" % input_year
    
if __name__ == '__main__': main()
