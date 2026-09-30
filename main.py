"""
main.py
-------
Algorithm Explorer - a menu-driven toolkit that shows how basic
problem-solving algorithms work, step by step.

Run with:  python main.py
"""
import logging

import array_techniques as at
import factoring_methods as fm
import number_algorithms as na
from history import SessionHistory, setup_logging
from quiz import run_quiz
from validators import read_choice, read_int, read_int_list

logger = logging.getLogger(__name__)
history = SessionHistory()


# ---------------------------------------------------------------
# Module 1a: Number algorithms (Unit 3)
# ---------------------------------------------------------------
def do_factorial():
    n = read_int("Enter n (0-500): ", 0, 500)
    if n <= 10:
        parts = " x ".join(str(i) for i in range(n, 0, -1)) or "1"
        print(f"{n}! = {parts} = {na.factorial(n)}")
    else:
        print(f"{n}! = {na.factorial(n)}")


def do_fibonacci_series():
    count = read_int("How many terms (1-50)? ", 1, 50)
    print("Series:", ", ".join(map(str, na.fibonacci_series(count))))


def do_reverse_number():
    n = read_int("Enter a whole number: ")
    print(f"Reversed: {na.reverse_number(n)}")


def do_base_conversion():
    n = read_int("Enter a non-negative number: ", 0)
    base = read_int("Convert to base (2-16): ", 2, 16)
    print(f"{n} in base {base} is {na.convert_base(n, base)}")


def do_swap():
    a = read_int("First value: ")
    b = read_int("Second value: ")
    a, b = na.swap_values(a, b)
    print(f"After swapping: first = {a}, second = {b}")


def do_char_to_number():
    text = input("Enter digits (e.g. 472): ").strip()
    print(f"As a number: {na.char_to_number(text)}")


def do_digit_info():
    n = read_int("Enter a whole number: ")
    print(f"Digits: {na.count_digits(n)}, sum of digits: {na.sum_of_digits(n)}")


NUMBER_MENU = {
    "1": ("Factorial", do_factorial),
    "2": ("Fibonacci series", do_fibonacci_series),
    "3": ("Reverse a number", do_reverse_number),
    "4": ("Base conversion", do_base_conversion),
    "5": ("Swap two values", do_swap),
    "6": ("Character to number", do_char_to_number),
    "7": ("Count and sum digits", do_digit_info),
}


# ---------------------------------------------------------------
# Module 1b: Factoring methods (Unit 4)
# ---------------------------------------------------------------
def do_gcd():
    a = read_int("First number: ", 0)
    b = read_int("Second number: ", 0)
    result, steps = fm.gcd_steps(a, b)
    print("Euclid's algorithm steps:")
    for step in steps:
        print("  ", step)
    print(f"GCD = {result}")
    if a > 0 and b > 0:
        print(f"LCM = {fm.lcm(a, b)}")


def do_prime_check():
    n = read_int("Enter a number: ")
    if fm.is_prime(n):
        print(f"{n} is prime.")
    elif n >= 2:
        print(f"{n} is not prime (smallest divisor: {fm.smallest_divisor(n)}).")
    else:
        print(f"{n} is not prime.")


def do_generate_primes():
    limit = read_int("Primes up to (max 100000): ", 2, 100000)
    primes = fm.generate_primes(limit)
    print(f"Found {len(primes)} primes:")
    print(", ".join(map(str, primes[:100])) + (" ..." if len(primes) > 100 else ""))


def do_prime_factors():
    n = read_int("Enter a number (2 or more): ", 2)
    print(f"Prime factors of {n}: {fm.prime_factors(n)}")


def do_square_root():
    n = read_int("Enter a non-negative number: ", 0)
    print(f"Square root (Newton's method): {fm.square_root(n):.6f}")


def do_power():
    base = read_int("Base: ")
    exponent = read_int("Exponent (0 or more): ", 0)
    print(f"{base}^{exponent} = {fm.power(base, exponent)}")


def do_nth_fibonacci():
    n = read_int("Which Fibonacci number (n)? ", 0, 10000)
    print(f"F({n}) = {fm.nth_fibonacci(n)}")


def do_random_numbers():
    seed = read_int("Seed number: ", 0)
    count = read_int("How many numbers (1-20)? ", 1, 20)
    low = read_int("Lowest value: ")
    high = read_int("Highest value: ", low)
    print("Numbers:", fm.lcg_random(seed, count, low, high))


FACTOR_MENU = {
    "1": ("GCD and LCM", do_gcd),
    "2": ("Prime check", do_prime_check),
    "3": ("Generate primes", do_generate_primes),
    "4": ("Prime factors", do_prime_factors),
    "5": ("Square root", do_square_root),
    "6": ("Raise to a power", do_power),
    "7": ("nth Fibonacci number", do_nth_fibonacci),
    "8": ("Pseudo-random numbers", do_random_numbers),
}


# ---------------------------------------------------------------
# Module 2: Array and collections (Unit 5)
# ---------------------------------------------------------------
def do_reverse_array():
    arr = read_int_list("Enter numbers (space or comma separated): ")
    print("Reversed:", at.reverse_array(arr))


def do_count():
    arr = read_int_list("Enter numbers: ")
    target = read_int("Number to count: ")
    print(f"{target} appears {at.count_occurrences(arr, target)} time(s).")


def do_min_max():
    arr = read_int_list("Enter numbers: ")
    smallest, biggest = at.min_max(arr)      # tuple unpacking
    print(f"Minimum = {smallest}, Maximum = {biggest}")


def do_remove_duplicates():
    arr = read_int_list("Enter numbers: ")
    ordered = sorted(arr)
    print("Sorted:", ordered)
    print("Without duplicates:", at.remove_duplicates_sorted(ordered))


def do_partition():
    arr = read_int_list("Enter numbers: ")
    pivot = read_int("Pivot value: ")
    smaller, equal, larger = at.partition_array(arr, pivot)
    print(f"Smaller: {smaller}\nEqual:   {equal}\nLarger:  {larger}")


def do_kth_smallest():
    arr = read_int_list("Enter numbers: ")
    k = read_int(f"k (1-{len(arr)}): ", 1, len(arr))
    print(f"The {na.ordinal(k)} smallest number is {at.kth_smallest(arr, k)}")


def do_set_operations():
    first = read_int_list("First list: ")
    second = read_int_list("Second list: ")
    for name, values in at.set_operations(first, second).items():
        print(f"  {name}: {values}")


def do_word_frequency():
    text = input("Enter a sentence: ")
    counts = at.word_frequency(text)
    if not counts:
        raise ValueError("No words found.")
    for word, count in sorted(counts.items()):
        print(f"  {word}: {count}")


ARRAY_MENU = {
    "1": ("Reverse a list", do_reverse_array),
    "2": ("Count occurrences", do_count),
    "3": ("Minimum and maximum", do_min_max),
    "4": ("Remove duplicates", do_remove_duplicates),
    "5": ("Partition around a pivot", do_partition),
    "6": ("K-th smallest element", do_kth_smallest),
    "7": ("Set operations on two lists", do_set_operations),
    "8": ("Word frequency (dictionary)", do_word_frequency),
}


# ---------------------------------------------------------------
# Menu helpers
# ---------------------------------------------------------------
def run_menu(title, options):
    """Show a sub-menu and run the chosen action until the user goes back."""
    while True:
        print(f"\n=== {title} ===")
        for key, (label, _) in options.items():
            print(f"  {key}. {label}")
        print("  0. Back")
        choice = read_choice("Choose an option: ", list(options) + ["0"])
        if choice == "0":
            return
        label, action = options[choice]
        try:
            action()
            history.record_action(label)
            logger.info("Used feature: %s", label)
        except ValueError as error:      # friendly message, no crash
            print(f"  ! {error}")
            logger.warning("Problem in %s: %s", label, error)


def do_quiz():
    run_quiz(history)
    logger.info("Quiz completed")


def do_history():
    print("\n--- Session History ---")
    print(history.summary())


def main():
    setup_logging()
    logger.info("Program started")
    print("=" * 40)
    print("   ALGORITHM EXPLORER")
    print("   Learn problem solving step by step")
    print("=" * 40)

    try:
        while True:
            print("\n=== MAIN MENU ===")
            print("  1. Number algorithms")
            print("  2. Factoring methods")
            print("  3. Arrays and collections")
            print("  4. Practice quiz")
            print("  5. Session history")
            print("  0. Exit")
            choice = read_choice("Choose an option: ", ["0", "1", "2", "3", "4", "5"])
            if choice == "1":
                run_menu("NUMBER ALGORITHMS", NUMBER_MENU)
            elif choice == "2":
                run_menu("FACTORING METHODS", FACTOR_MENU)
            elif choice == "3":
                run_menu("ARRAYS AND COLLECTIONS", ARRAY_MENU)
            elif choice == "4":
                do_quiz()
            elif choice == "5":
                do_history()
            else:
                break
    except (KeyboardInterrupt, EOFError):
        print()                          # Ctrl+C / Ctrl+D: exit politely

    logger.info("Program ended")
    print("Goodbye! Keep practising.")


if __name__ == "__main__":
    main()
