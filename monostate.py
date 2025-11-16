class StrReprMixin:
    def __str__(self):
        params = ''.join([f'{k}={v}' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class MonosStateSimple(StrReprMixin):
    _state: dict = {}

    def __init__(self, nome=None, sobrenome=None):
        self.__dict__ = self._state

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


m1 = MonosStateSimple('Rafael')
m2 = MonosStateSimple()
print(m1)
print(m2)
