from typing import Dict


class Singleton(type):
    _instances: Dict = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'


if __name__ == '__main__':
    as1 = AppSettings()
    as1.tema = 'O tema claro'

    print(as1.tema)
    as2 = AppSettings()
    print(as1.tema)
    print(as2.tema)
