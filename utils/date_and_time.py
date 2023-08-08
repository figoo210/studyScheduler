
import calendar
from datetime import date, datetime, time, timedelta

# get today's date
d = date.today()

# get day name in english
def get_day_name():
    day_name = calendar.day_name[d.weekday()]
    return day_name

# Get day name from string date
def get_day_name_from_string_date(date_string, date_format="%d-%m-%Y"):
    date = datetime.strptime(date_string, date_format)
    return calendar.day_name[date.weekday()]


def get_date_from_string(date_str, date_format="%d-%m-%Y"):
    return datetime.strptime(date_str, date_format).date()

def get_string_from_date(date_obj, date_format="%d-%m-%Y"):
    return date_obj.strftime(date_format)

def add_time_hours(time_obj, hours):
    t = time_obj
    hours_to_add = timedelta(hours=hours)
    added_hours = (t.hour + hours_to_add.seconds // 3600) % 24
    added_minutes = t.minute
    t = time(added_hours, added_minutes)
    return t

def delete_time_minutes(time_obj, minutes):
    t = time_obj
    minus_minutes = timedelta(minutes=minutes)
    remainder_minutes = (t.minute - minus_minutes.seconds // 60) % 60
    # If remainder is < 0, subtract 1 from hour and set minutes to 60 + remainder
    if remainder_minutes == 59:
        subtracted_hour = (t.hour - 1) % 24
    else:
        subtracted_hour = t.hour

    t = time(subtracted_hour, remainder_minutes)
    return t


def get_day_of_week_dates(start, end, day_of_week):
    dates = []
    current = start
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    while current <= end:
        if weekdays[current.weekday()] == day_of_week:
            dates.append(current)
        current += timedelta(days=1)
    return dates

