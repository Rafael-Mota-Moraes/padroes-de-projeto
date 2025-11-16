from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: pass


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self._total = float(total)
        self._discount = discount

    @property
    def total(self):
        return self._total

    @property
    def total_with_discount(self):
        return self._discount.calculate(self.total)


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value - (value * 0.5)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float) -> float:
        return value


if __name__ == '__main__':
    twenty_percent = TwentyPercent()
    fifty_percent = TwentyPercent()
    order = Order(1000, twenty_percent)
    order2 = Order(1000, fifty_percent)
    print(order.total, order.total_with_discount)
    print(order2.total, order2.total_with_discount)
