from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    @abstractmethod
    def print_content(self) -> None: pass

    @abstractmethod
    def get_price(self) -> float: pass

    def add(self, child: BoxStructure) -> None: pass

    def remove(self, child: BoxStructure) -> None: pass


class Box(BoxStructure):
    def __init__(self, name):
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([
            child.get_price() for child in self._children
        ])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


c1 = Product('camiseta 1', 10)
c2 = Product('camiseta 2', 20)
c3 = Product('camiseta 3', 30)
c4 = Product('camiseta 4', 40)

cx = Box('caixa de camiseta')
cx.add(c1)
cx.add(c2)
cx.add(c3)
cx.add(c4)
cx.print_content()


sm1 = Product('Smartphone 1', 9000)
sm2 = Product('Smartphone 2', 1500)
sm3 = Product('Smartphone 3', 6500)
cx2 = Box('caixa smartphones')
cx2.add(sm1)
cx2.add(sm2)
cx2.add(sm3)
cx2.print_content()

print()

cx_grande = Box('Caixa grande')
cx_grande.add(cx)
cx_grande.add(cx2)
cx_grande.print_content()
