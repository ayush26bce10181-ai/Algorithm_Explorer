"""
number_algorithms.py
--------------------
Fundamental algorithms from Unit 3 of CSE1021:
exchange values, counting, summation, factorial, Fibonacci,
reverse, base conversion and character-to-number conversion.
"""

DIGITS = "0123456789ABCDEF"


def swap_values(a, b):
    """Exchange two values using tuple assignment (no temp variable needed)."""
    a, b = b, a
    return a, b


def count_digits(n):
    """Count how many digits a whole number has."""
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count


def sum_of_digits(n):
    """Add up all the digits of a whole number (summation)."""
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total


def factorial(n):
    """Return n! (n must be 0 or more)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci_series(count):
    """Return the first `count` Fibonacci numbers: 0, 1, 1, 2, 3, 5, ..."""
    if count < 0:
        raise ValueError("Count cannot be negative.")
    series = []
    a, b = 0, 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b
    return series


def reverse_number(n):
    """Reverse the digits of a number, e.g. 1234 -> 4321."""
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n = n // 10
    return sign * reversed_n


def convert_base(n, base):
    """Convert a non-negative whole number to another base (2 to 16)."""
    if n < 0:
        raise ValueError("Only non-negative numbers can be converted.")
    if base < 2 or base > 16:
        raise ValueError("Base must be between 2 and 16.")
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        result = DIGITS[n % base] + result   # remainder becomes next digit
        n = n // base
    return result


def char_to_number(text):
    """Convert a string of digits such as '472' into the number 472
    without using int(). Uses the character codes (ord)."""
    if text == "":
        raise ValueError("Nothing to convert.")
    number = 0
    for ch in text:
        if ch not in "0123456789":
            raise ValueError(f"'{ch}' is not a digit.")
        number = number * 10 + (ord(ch) - ord("0"))
    return number


def letter_position(ch):
    """Return the position of a letter in the alphabet (a=1, b=2, ...)."""
    if len(ch) != 1 or not ch.isalpha() or not ch.isascii():
        raise ValueError("Please enter a single English letter.")
    return ord(ch.lower()) - ord("a") + 1


def ordinal(n):
    """Return n with its English ending: 1 -> '1st', 2 -> '2nd', 13 -> '13th'."""
    if 10 <= n % 100 <= 20:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"
