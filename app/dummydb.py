from core.dummydb import Singleton


def get_club():
    return Club()


class Club(metaclass=Singleton):

    def __init__(self):
        self.playing = None
        self.playlist = []
        self.people = {}

    def __str__(self):
        if self.playing is None:
            return 'Музыка выключена. В зале тишина'

        ret = 'Сейчас играет: [{}] {}\n'.format(self.playing, self.playlist[self.playing].value.capitalize())

        if not self.people:
            ret += 'В клубе никого нет.'
            return ret

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
