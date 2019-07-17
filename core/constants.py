from enum import IntEnum, Enum


class Style(IntEnum):
    RNB = 1
    ELECTROHOUSE = 2
    POP = 3


class CommandName(Enum):
    EXIT_COMMAND = '/exit'
    STATE_COMMAND = '/state'
    ADD_USER_COMMAND = '/adduser'
