from app.constants import Activity, StyleType
from app.models import Style
from core.dummydb import Singleton

# TODO: /addstyle command
EXISTING_STYLES = {
    'hip-hop': Style(
        name='hip-hop',
        style_type=StyleType.RNB,
        dance_description='покачивания телом вперед и назад, ноги в полу-присяде, руки согнуты в локтях, головой вперед-назад',
    ),
    'rnb': Style(
        name='rnb',
        style_type=StyleType.RNB,
        dance_description='покачивания телом вперед и назад, ноги в полу-присяде, руки согнуты в локтях, головой вперед-назад',
    ),
    'electrodance': Style(
        name='electrodance',
        style_type=StyleType.ELECTROHOUSE,
        dance_description='покачивание туловищем вперед-назад, почти нет движения головой, круговые движения - вращения руками, ноги двигаются в ритме',
    ),
    'house': Style(
        name='house',
        style_type=StyleType.ELECTROHOUSE,
        dance_description='покачивание туловищем вперед-назад, почти нет движения головой, круговые движения - вращения руками, ноги двигаются в ритме',
    ),
    'pop': Style(
        name='pop',
        style_type=StyleType.POP,
        dance_description='плавные движения туловищем, руками, ногами и головой'
    ),
}


class Club(metaclass=Singleton):

    def __init__(self):
        self.playing = None
        self.playlist = []
        self.people = []

    def __str__(self):
        ret = 'Музыка выключена. Никто не танцует.\n'
        if self.playing is not None:
            ret = 'Сейчас играет: [{}] {}\n'.format(self.playing, self.playlist[self.playing].capitalize())

        if not self.people:
            ret += 'В клубе никого нет.'
            return ret

        for person in self.people:
            ret += '{} сейчас {}\n'.format(person.name, person.activity.value)

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
                self.playlist[self.playing].capitalize(),
            ))
        else:
            print('Музыка выключена. В зале тишина.')
        for index, song in enumerate(self.playlist):
            print('[{}] {}'.format(index, song.capitalize()))

    def update_persons_activities(self, alone_person=None):
        style = self._get_style()
        if alone_person:
            alone_person.activity = self._get_activity(alone_person, style)
            return

        for person in self.people:
            person.activity = self._get_activity(person, style)

    def _get_style(self):
        return None if self.playing is None else self.playlist[self.playing]

    def _get_activity(self, person, style):
        style = style and person.styles.get(style) or None

        return style and Activity.DANCING or Activity.DRINKING


def get_club():
    return Club()
