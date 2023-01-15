from dataclasses import dataclass


@dataclass
class Grid:
    width: int
    height: int

    def __post_init__(self):
        self._body: list[list] = [["X" for _ in range(self.width)] for _ in range(self.height)]

    @property
    def body(self):
        return self._body
