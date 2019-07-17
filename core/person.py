from dataclasses import dataclass, field
from typing import List

from core.constants import Style


@dataclass(frozen=True)
class Person:
    name: str
    # skills: List[Skill] = field(default_factory=list)

    def __post_init__(self):
        pass


@dataclass(frozen=True)
class Song:
    name: str
    style: Style


@dataclass(frozen=True)
class Skill:
    name: str
    style: Style
