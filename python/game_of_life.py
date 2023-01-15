from dataclasses import dataclass


@dataclass
class Grid:
    width: int
    height: int

    def __post_init__(self):
        self._body: list[list[Cell]] = [[Cell() for _ in range(self.width)] for _ in range(self.height)]

    @property
    def body(self):
        return self._body


@dataclass
class Cell:
    def __post_init__(self):
        self._state = "X"

    @property
    def state(self):
        return self._state

    def change_state(self):
        self._state = "0" if self.state == "X" else "X"
