from strenum import StrEnum
from database import db

class Program(StrEnum):
    regularity = "Regularity"
    affiliation = "Affiliation"
    open_education = "Open Education"


class ProgramEnum(db.TypeDecorator):
    """
    Enables passing in a Python enum and storing the enum's *value* in the db.
    The default would have stored the enum's *name* (ie the string).
    """
    impl = db.String(20)

    def __init__(self, enumtype, *args, **kwargs):
        super(ProgramEnum, self).__init__(*args, **kwargs)
        self._enumtype = enumtype

    def process_bind_param(self, value, dialect):
        if isinstance(value, str):
            return value

        return value.value

    def process_result_value(self, value, dialect):
        return self._enumtype(value)