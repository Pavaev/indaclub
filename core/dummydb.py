from dataclasses import dataclass, field
from typing import List

from core.person import Person


def get_db():
    return Club()


class Singleton(object):
    obj = None

    def __new__(cls):
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj


@dataclass
class Club(Singleton):
    person_list: List[Person] = field(default_factory=list)
