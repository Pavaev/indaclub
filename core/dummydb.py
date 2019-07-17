from dataclasses import dataclass, field
from typing import List, Set, Dict

from core.constants import Style
from core.person import Person


def get_club():
    return Club()


class Singleton(type):
    _obj = None

    def __call__(cls, *args, **kwargs):
        if not cls._obj:
            cls._obj = super().__call__(*args, **kwargs)
        return cls._obj


class Club(metaclass=Singleton):

    def __init__(self):
        self.playing = None
        self.playlist = []
        self.people = {}

    def __str__(self):
        if not self.people:
            return 'В клубе никого нет.'

        if self.playing is None:
            return 'Музыка выключена. В зале тишина. Возле барной стойки толпится народ.'

        ret = 'Сейчас играет: [{}] {}'.format(self.playing, self.playlist[self.playing].value.capitalize())
        for person in self.people.values():
            ret += 'Посетитель {} находится в {}\n'.format(person.name, person.state.value.capitalize())

        return ret

    @property
    def playlist_length(self):
        return len(self.playlist)

    def show_playlist(self):
        if not self.playlist:
            print('Плейлист пуст.')
            return
        if self.playing is not None:
            print('Сейчас играет: [{}] {}.'.format(
                self.playing,
                self.playlist[self.playing].value.capitalize(),
            ))
        else:
            print('Музыка остановлена.')
        for index, song in enumerate(self.playlist):
            print('[{}] {}'.format(index, song.value.capitalize()))

