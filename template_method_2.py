from abc import ABC, abstractmethod


class Pizza(ABC):
    def prepare(self):
        """ Template method """
        self.add_ingredients()  # abstract
        self.cook()  # abstract
        self.cut()  # concreto
        self.serve()  # concreto

    def cut(self):
        print(f'{self.__class__.__name__}: cortando pizza')

    def serve(self):
        print(f'{self.__class__.__name__}: servindo pizza')

    @abstractmethod
    def add_ingredients(self): pass

    @abstractmethod
    def cook(self): pass


class StylishPizza(Pizza):
    def add_ingredients(self):
        print(f'{self.__class__.__name__}: adicionado ingredientes da pizza')

    def cook(self):
        print(f'{self.__class__.__name__}: cozinhando a pizza')


p = StylishPizza()
p.prepare()
