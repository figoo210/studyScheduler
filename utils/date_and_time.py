
import calendar
from datetime import date, datetime

# get today's date
d = date.today()

# get day name in english
def get_day_name():
    day_name = calendar.day_name[d.weekday()]
    return day_name

def get_date_from_string(date_str, date_format="%d-%m-%Y"):
    return datetime.strptime(date_str, date_format).date()

def get_string_from_date(date_obj, date_format="%d-%m-%Y"):
    return date_obj.strftime(date_format)
