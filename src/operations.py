from typing import Callable, NamedTuple

class Operation(NamedTuple):
    name: str
    func: Callable[[int, int], int]

def add(a: float|int, b: float|int) -> float|int:
    return a + b


def subtract(a: float|int, b: float|int) -> float|int:
    return a - b

operations = [
    Operation(name="Add", func=add),
    Operation(name="Subtract", func=subtract),
]
    
def get_operation_from_user() -> Operation:
    print("Available operations:")
    for idx, operation in enumerate(operations, 1):
        print(f"{idx}. {operation.name}")
    
    while True:
        try:
            operation_id = int(input("Enter an operation id: ")) - 1
            if 0 <= operation_id < len(operations):
                result = operations[operation_id]
                print(f"Selected operation: {result.name}")
                return result
            else:
                print("Invalid ID. Please select a valid operation.")
        except ValueError:
            print("Please enter a valid number.")
