from enum import Enum


class StyleType(Enum):
    RNB = 'rnb'
    ELECTROHOUSE = 'electrohouse'
    POP = 'pop'


class Activity(Enum):
    DANCING = 'танцует'
    DRINKING = 'пьет'


class CommandName(Enum):
    EXIT_COMMAND = '/exit'
    STATE_COMMAND = '/state'
    ADD_PERSON_COMMAND = '/addperson'
    PLAY_COMMAND = '/play'
    ADD_SONG_COMMAND = '/addsong'
    PLAYLIST_COMMAND = '/playlist'
    STOP_COMMAND = '/stop'
