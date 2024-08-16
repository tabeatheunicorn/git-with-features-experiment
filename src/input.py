def get_number_from_input(message:str = "Enter a number: ")-> int:
    """
    Get a number from the user input
    :return: int
    """
    number = input(message)
    return int(number)