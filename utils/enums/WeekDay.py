from strenum import StrEnum
from database import db


class WeekDay(StrEnum):
    sat = "Saturday"
    sun = "Sunday"
    mon = "Monday"
    tue = "Tuesday"
    wed = "Wednesday"
    thu = "Thursday"
    fri = "Friday"


class WeekDayEnum(db.TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """
    impl = db.String(10)
    cache_ok = True

    def __init__(self, enumtype, *args, **kwargs):
        super(WeekDayEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            return value

        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)


def get_translated_weekdays():
    return {
        "Saturday": "السبت",
        "Sunday": "الأحد",
        "Monday": "الأثنين",
        "Tuesday": "الثلاثاء",
        "Wednesday": "الاربعاء",
        "Thursday": "الخميس",
        "Friday": "الجمعة"
    }
