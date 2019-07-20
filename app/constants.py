from enum import Enum


class StyleType(Enum):
    RNB = 'rnb'
    ELECTROHOUSE = 'electrohouse'
    POP = 'pop'


class Activity(Enum):
    DANCING = 'танцует'
    DRINKING = 'пьет'


class CommandName(Enum):
    PLAY_COMMAND = '/play'
    STOP_COMMAND = '/stop'
    ADD_SONG_COMMAND = '/addsong'
    PLAYLIST_COMMAND = '/playlist'

    ADD_PERSON_COMMAND = '/addperson'

    EXIT_COMMAND = '/exit'
    STATE_COMMAND = '/state'
    HELP_COMMAND = '/help'
