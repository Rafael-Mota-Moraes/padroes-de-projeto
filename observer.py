from abc import ABC, abstractmethod
from typing import List, Dict


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass


class IObservable(ABC):
    @property
    def state(self): pass

    @abstractmethod
    def add_observer(self, observer: IObserver): pass

    @abstractmethod
    def remove_observer(self, observer: IObserver): pass

    @abstractmethod
    def notify_observers(self, observer: IObserver): pass


class WeatherStation(IObservable):
    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return

        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update()
        print()


class Smartphone(IObserver):
    def __init__(self, name, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto {observable_name} acabou de ser atualizado => {self.observable.state}')


station = WeatherStation()
smartphone = Smartphone('iPhone', station)
outro_smartphone = Smartphone('Samsumg', station)

station.add_observer(smartphone)
station.add_observer(outro_smartphone)

station.state = {'temperature': '30'}
station.state = {'temperature': '32'}
station.remove_observer(outro_smartphone)
station.reset_state()
