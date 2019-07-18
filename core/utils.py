import random
import datetime
from calendar import monthlen


def get_random_birthdate():
    year = random.randint(1960, 2001)
    month = random.randint(1, 12)
    month_lenght = monthlen(year, month)

    day = random.randint(1, 31)
    if day > month_lenght:
        day = month_lenght
    return datetime.datetime(year=year, month=month, day=day)


def is_integer(value, only_positive=False):
    try:
        value = int(value)
    except (TypeError, ValueError):
        return False

    if only_positive and value < 0:
        return False
    return True
