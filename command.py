from __future__ import annotations
from abc import ABC, abstractmethod


class Light:
    """ receiver """

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'A luz {self.name} que está no {self.room_name} está ligada')

    def off(self) -> None:
        print(f'A luz {self.name} que está no {self.room_name} está desligada')

    def change_color(self, color: str) -> None:
        self.color = color
        print(
            f'A luz {self.name} que está no {self.name} agora tem a cor {self.color}')


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None: pass

    @abstractmethod
    def undo(self) -> None: pass


class LightOnCommand(ICommand):
    def __init__(self, light: Light):
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class RemoteController:
    """ Invoker """

    def __init__(self) -> None:
        self._buttons: dict[str, ICommand] = {}

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:
        self._buttons[name].execute()

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()


bedroom_light = Light('Luz do quarto', 'Quarto')
bethroom_light = Light('Luz do banheiro', 'Banheiro')

bedroom_light_on = LightOnCommand(bedroom_light)
bethroom_light_on = LightOnCommand(bethroom_light)

remote = RemoteController()
remote.button_add_command('first_button', bedroom_light_on)
remote.button_execute('first_button')
remote.button_undo('first_button')

remote.button_add_command('second_button', bedroom_light_on)
remote.button_execute('second_button')
remote.button_undo('second_button')
