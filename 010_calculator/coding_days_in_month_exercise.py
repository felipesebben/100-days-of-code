def is_leap(year):
    """Define if input year is a leap year or not."""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Return number of days in a month of a year and considers whether it 
    is a leap year or not.
    """
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not is_leap(year):
        return month_days[month - 1]
    elif is_leap(year):
        if month == 2:
            return month_days[month - 1] + 1
        else:
            return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
