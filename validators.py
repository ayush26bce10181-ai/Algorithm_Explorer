"""
validators.py
-------------
Input checking so the program never crashes on bad input.
"""


def parse_int_list(text):
    """Turn '5, 3 8,1' into [5, 3, 8, 1]. Raises ValueError if invalid."""
    pieces = text.replace(",", " ").split()
    if not pieces:
        raise ValueError("The list is empty.")
    numbers = []
    for piece in pieces:
        try:
            numbers.append(int(piece))
        except ValueError:
            raise ValueError(f"'{piece}' is not a whole number.")
    return numbers


def read_int(prompt, min_value=None, max_value=None):
    """Keep asking until the user types a whole number in range."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("  ! Please enter a whole number.")
            continue
        if min_value is not None and value < min_value:
            print(f"  ! Number must be at least {min_value}.")
            continue
        if max_value is not None and value > max_value:
            print(f"  ! Number must be at most {max_value}.")
            continue
        return value


def read_int_list(prompt):
    """Keep asking until the user types a valid list of whole numbers."""
    while True:
        try:
            return parse_int_list(input(prompt))
        except ValueError as error:
            print(f"  ! {error}")


def read_choice(prompt, valid_choices):
    """Keep asking until the user picks one of the valid choices."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("  ! Invalid choice, try again.")
