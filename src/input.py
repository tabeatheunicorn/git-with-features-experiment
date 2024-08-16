def get_number_from_input(message:str = "Enter a number: ")-> int:
    """
    Get a number from the user input. If the input is not a number, 
    it will continue to ask the user to enter a valid number.
    :return: int
    """
    while True:
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")