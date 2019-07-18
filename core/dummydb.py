class Singleton(type):
    _obj = None

    def __call__(cls, *args, **kwargs):
        if not cls._obj:
            cls._obj = super().__call__(*args, **kwargs)
        return cls._obj
