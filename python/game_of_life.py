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
        self.state = CellState()

    def change_state(self):
        self.state.change_state()


@dataclass
class CellState:
    STATE_ALIVE = "0"
    STATE_DEAD = "X"

    def __post_init__(self):
        self._state = self.STATE_DEAD

    def __call__(self):
        return self._state

    def __eq__(self, other):
        return self() == other

    def change_state(self):
        self._state = self.STATE_ALIVE if self._state == self.STATE_DEAD else self.STATE_DEAD
