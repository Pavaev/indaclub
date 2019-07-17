from abc import ABCMeta, abstractclassmethod


class SimpleCommand(metaclass=ABCMeta):
    @abstractclassmethod
    def __call__(cls):
        raise NotImplementedError()


class Command(metaclass=ABCMeta):
    @abstractclassmethod
    def __call__(cls, *args):
        raise NotImplementedError()
