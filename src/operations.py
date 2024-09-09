from typing import Callable, NamedTuple

class Operation(NamedTuple):
    name: str
    func: Callable[[int, int], int]

def add(a: float|int, b: float|int) -> float|int:
    return a + b
