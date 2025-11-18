from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.operation_1()
        self.operation_2()
        self.base_class_method()
        print()

    def base_class_method(self):
        print('Método da classe base')

    def hook(self): pass

    @abstractmethod
    def operation_1(self): pass

    @abstractmethod
    def operation_2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Agora o hook tem implementação')

    def operation_1(self):
        print('Operação 1 concluída')

    def operation_2(self):
        print('Operação 2 concluída')


class ConcreteClass2(Abstract):
    def operation_1(self):
        print('Operação 1 concluída de maneira diferente')

    def operation_2(self):
        print('Operação 2 concluída de maneira diferente')


c1 = ConcreteClass1()
c1.template_method()

c2 = ConcreteClass2()
c2.template_method()
