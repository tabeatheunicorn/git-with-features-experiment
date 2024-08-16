from operator import add
from input import get_number_from_input


def calculator_main():
    print("I can calculate")
    print("Let's start with addition")
    a = get_number_from_input("Enter the first number: ")
    b = get_number_from_input("Enter the second number: ")
    result = add(a, b)
    print(f"The result of {a} + {b} is {result}")
    
if __name__ == "__main__":
    calculator_main()
    