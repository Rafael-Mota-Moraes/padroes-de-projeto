from __future__ import annotations
from typing import List, Dict


class Client:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._addresses: List = []
        self.address_number: str
        self.address_detail: str

    def add_adress(self, address: Address) -> None:
        self._addresses.append(address)

    def list_addresses(self) -> None:
        for address in self._addresses:
            address.show_address(self.address_number, self.address_detail)


class Address:
    def __init__(self, street: str, neighbourhood: str, zip_code: str) -> None:
        self._street = street
        self._neighbourhood = neighbourhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, adress_details: str) -> None:
        print(self._street, address_number, adress_details,
              self._neighbourhood, self._zip_code)


class AddressFactory:
    _addresses: Dict = {}

    def _get_key(self, **kwargs):
        return ''.join(kwargs.values())

    def get_address(self, **kwargs) -> Address:
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
        except KeyError:
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight
            print('criando')

        return address_flyweight


address_factory = AddressFactory()
a1 = address_factory.get_address(
    street='Av. Brasil', neighbourhood='Centro', zip_code='00000-00')
a2 = address_factory.get_address(
    street='Av. Brasil', neighbourhood='Centro', zip_code='00000-00')

rafa = Client('Rafa')
rafa.address_number = '50'
rafa.address_detail = 'Casa'
rafa.add_adress(a1)
rafa.list_addresses()
