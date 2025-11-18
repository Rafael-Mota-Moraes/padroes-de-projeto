from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """ Context """

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self):
        self.state.pending()

    def aprove(self):
        self.state.aprove()

    def reject(self):
        self.state.reject()


class OrderState(ABC):
    def __init__(self, order: Order):
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def aprove(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass


class PaymentPending(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print('Pagamento já pendente, nada para fazer')

    def aprove(self) -> None:
        self.order.state = PaymentAproved(self.order)
        print("Pagamento aprovado")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")


class PaymentAproved(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("Pagamento pendente")

    def aprove(self) -> None:
        print("Pagamento já aprovado, nada para fazer")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Pagamento recusado")


class PaymentRejected(OrderState):
    def __init__(self, order: Order):
        self.order = order

    def pending(self) -> None:
        print("Pagamento recusado, não podemos fazer nada")

    def aprove(self) -> None:
        print("Pagamento recusado, não podemos fazer nada")

    def reject(self) -> None:
        print("Pagamento recusado, não podemos fazer nada")


o = Order()
o.pending()
o.aprove()
o.aprove()
