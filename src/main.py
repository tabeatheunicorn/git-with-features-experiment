from operator import add
from input import get_number_from_input
from operations import get_operation_from_user


def calculator_main():
    print("I can calculate")
    a = get_number_from_input("Enter the first number: ")
    b = get_number_from_input("Enter the second number: ")
    
    operation = get_operation_from_user()
    print(f"The result of {operation.name} with {a}, {b} is {operation.func(a, b)}")
    
if __name__ == "__main__":
    calculator_main()
    