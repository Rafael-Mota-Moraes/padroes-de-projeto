from copy import deepcopy
from typing import List


class StrReprMixin:
    def __str__(self):
        params = ''.join([f'{k}={v}, ' for k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self):
        return self.__str__()


class Address(StrReprMixin):
    def __init__(self, street: str, number: str):
        self.street = street
        self.number = number


class Person(StrReprMixin):
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname
        self.addresses: List[Address] = []

    def add_address(self, address: Address) -> None:
        self.addresses.append(address)

    def clone(self):
        return deepcopy(self)


rafa = Person('Rafael', 'Mota')
endereco_rafa = Address('Av. Brasil', '10')
rafa.add_address(endereco_rafa)

esposa = rafa.clone()
esposa.firstname = 'Maria'

print(rafa)
print(esposa)
