from enum import IntEnum
from database import db

class Division(IntEnum):
    first = 1
    second = 2
    third = 3
    fourth = 4


class DivisionEnum(db.TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """
    impl = db.Integer
    cache_ok = True

    def __init__(self, enumtype, *args, **kwargs):
        super(DivisionEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, int):
            return value

        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)


def get_translated_divisions():
    return {
        "1": "الفرقة الأولى",
        "2": "الفرقة الثانية",
        "3": "الفرقة الثالثة",
        "4": "الفرقة الرابعة",
    }
