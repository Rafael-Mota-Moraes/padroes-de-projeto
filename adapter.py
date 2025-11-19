from abc import ABC, abstractmethod


class IControl(ABC):
    @abstractmethod
    def top(self) -> None: pass

    @abstractmethod
    def right(self) -> None: pass

    @abstractmethod
    def down(self) -> None: pass

    @abstractmethod
    def left(self) -> None: pass


class NewControl:
    def top(self) -> None:
        print("top")

    def right(self) -> None:
        print("right")

    def down(self) -> None:
        print("down")

    def left(self) -> None:
        print("left")


class ControlAdapter:
    def __init__(self, new_control: NewControl):
        self.new_control = new_control

    def top(self) -> None:
        self.new_control.top()

    def right(self) -> None:
        self.new_control.right()

    def down(self) -> None:
        self.new_control.down()

    def left(self) -> None:
        self.new_control.left()


control = NewControl()
c1 = ControlAdapter(control)
c1.top()
c1.down()
