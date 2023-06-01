
import calendar
from datetime import date

# get today's date
d = date.today()
print('Date is:', d)

# get day name in english
def get_day_name():
    day_name = calendar.day_name[d.weekday()]
    print('Weekday name is:', day_name)
    return day_name
