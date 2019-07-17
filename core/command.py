from abc import ABCMeta, abstractmethod


class SimpleCommand(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def __call__():
        raise NotImplementedError()


class Command(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def __call__(*args):
        raise NotImplementedError()
