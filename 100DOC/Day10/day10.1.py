def is_leap(year):
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


# TODO: Add more code here 👇
def days_in_month(years, months):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(years) == True:
        month_days[1] = 29
        no_of_days = month_days[months - 1]
        return no_of_days
    else:
        no_of_days = month_days[months - 1]
        return no_of_days


# 🚨 Do NOT change any of the code below
year = int(input('Enter a Year'))  # Enter a year
month = int(input('Enter the month'))  # Enter a month
days = days_in_month(year, month)
print(days)

