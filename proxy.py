from __future__ import annotations

from abc import ABC, abstractmethod
from time import sleep
from typing import List, Dict


class IUser(ABC):
    """ Subject interface """

    firstname: str
    lastname: str

    @abstractmethod
    def get_addresses(self) -> List[Dict]: pass

    @abstractmethod
    def get_all_user_data(self) -> Dict: pass


class RealUser(IUser):
    def __init__(self, firstname: str, lastname: str):
        sleep(2)  # simulando uma requisição
        self.firstname = firstname
        self.lastname = lastname

    def get_addresses(self) -> List[Dict]:
        sleep(2)  # simulando uma requisição
        return [
            {'rua': 'Av. Brasil', 'numero': 500}
        ]

    def get_all_user_data(self) -> Dict:
        return {'cpf': '111.111.111-11', 'rg': '3142412'}


class UserProxy(IUser):
    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

        self._real_user: RealUser
        self._cached_addresses: List[Dict]
        self._all_user_data: Dict

    def get_real_user(self) -> None:
        if not hasattr(self, '_real_user'):
            self._real_user = RealUser(self.firstname, self.lastname)

    def get_addresses(self):
        self.get_real_user()
        if not hasattr(self, '_cached_addresses'):
            self._cached_addresses = self._real_user.get_addresses()

        return self._cached_addresses

    def get_all_user_data(self):
        self.get_real_user()
        if not hasattr(self, '_all_user_data'):
            self._all_user_data = self._real_user.get_all_user_data()

        return self._all_user_data


u = UserProxy('Rafael', 'Mota')
print(u.firstname)
print(u.lastname)
print(u.get_all_user_data())
print(u.get_addresses())
