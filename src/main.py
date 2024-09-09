from input import get_number_from_input
from operations import subtract


def calculator_main():
    print("Let's subtract two numbers!")
    a = get_number_from_input("Enter the first number: ")
    b = get_number_from_input("Enter the second number: ")
    result = subtract(a, b)
    print(f"The result of {a} - {b} is {result}")
    
if __name__ == "__main__":
    calculator_main()
    