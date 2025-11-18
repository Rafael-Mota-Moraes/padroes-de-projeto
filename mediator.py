from __future__ import annotations
from abc import ABC, abstractmethod


class Colleague(ABC):
    def __init__(self):
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None: pass

    @abstractmethod
    def direct(self, msg: str) -> None: pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self.mediator = mediator

    def broadcast(self, msg: str) -> None:
        self.mediator.broadcast(self, msg)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, colleague: Colleague, msg: str) -> None:
        ...

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, msg: str) -> None:
        ...


class Chatroom(Mediator):
    def __init__(self):
        self.colleagues = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague, msg):
        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} disse: {msg}')

    def direct(self, sender, receiver, msg):
        if not self.is_colleague(sender):
            return

        receiver_obj = [
            c for c in self.colleagues if c.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} para {receiver_obj[0].name}: {msg}')


chat = Chatroom()
p1 = Person('João', chat)
p2 = Person('Maria', chat)

chat.add(p1)
chat.add(p2)
p1.broadcast('teste')
p2.broadcast('maria')

chat.direct(p1, 'Maria', 'Teste')
