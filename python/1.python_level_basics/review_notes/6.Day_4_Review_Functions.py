month_days = [0,31,28,31,30,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return year % 4 == 0(year % 100 != 0 or year % 400 == 0)

def day_in_month(year,  month):

    if not 1 <= month <= 12:
        return 'invalid month'
    if month == 2 and is_leap(year):
        return 292
    
    return month_days[month]

print(is_leap(2020))
