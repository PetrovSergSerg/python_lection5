import datetime
from random import randint, choice
import re


def get_random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=randint(0, int((end - start).total_seconds())),
    )


def get_random_word(alphabet: str, length: int):
    """Generate a random word on alphabet with given length"""
    return ''.join([choice(alphabet) for i in range(length)])


def get_random_email(alphabet: str):
    """Generate random email using function get_random_word(alphabet, length)"""
    return get_random_word(alphabet, randint(3, 10)) + '@' + get_random_word(alphabet, randint(2, 10)) + '.ru'


def clear(string):
    return re.sub("[() -]", "", string)


def xstr(string):
    if string is None:
        return ""
    return str(string)
