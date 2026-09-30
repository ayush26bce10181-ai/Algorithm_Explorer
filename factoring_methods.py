"""
factoring_methods.py
--------------------
Algorithms from Unit 4 of CSE1021: square root, smallest divisor, GCD,
primes, prime factors, pseudo-random numbers, large powers and the
nth Fibonacci number.
"""


def square_root(n, tolerance=1e-10, max_steps=100):
    """Find the square root using Newton's method (guess, then improve)."""
    if n < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    if n == 0:
        return 0.0
    guess = n / 2 if n >= 1 else 1.0
    for _ in range(max_steps):
        if abs(guess * guess - n) <= tolerance:
            break
        guess = (guess + n / guess) / 2      # average of guess and n/guess
    return guess


def smallest_divisor(n):
    """Return the smallest divisor of n that is greater than 1."""
    if n < 2:
        raise ValueError("Number must be 2 or more.")
    i = 2
    while i * i <= n:          # only need to check up to sqrt(n)
        if n % i == 0:
            return i
        i += 1
    return n                   # n itself is prime


def gcd(a, b):
    """Greatest common divisor using Euclid's algorithm."""
    if a < 0 or b < 0:
        raise ValueError("Numbers must not be negative.")
    while b != 0:
        a, b = b, a % b
    return a


def gcd_steps(a, b):
    """Same as gcd() but also returns each division step as text."""
    if a < 0 or b < 0:
        raise ValueError("Numbers must not be negative.")
    steps = []
    while b != 0:
        steps.append(f"{a} = {a // b} x {b} + {a % b}")
        a, b = b, a % b
    return a, steps


def lcm(a, b):
    """Least common multiple, using the GCD."""
    if a <= 0 or b <= 0:
        raise ValueError("Numbers must be positive.")
    return a * b // gcd(a, b)


def is_prime(n):
    """Check whether n is prime by trial division."""
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def generate_primes(limit):
    """All primes up to `limit` using the Sieve of Eratosthenes."""
    if limit < 2:
        return []
    is_p = [True] * (limit + 1)
    is_p[0] = is_p[1] = False
    i = 2
    while i * i <= limit:
        if is_p[i]:
            for multiple in range(i * i, limit + 1, i):
                is_p[multiple] = False
        i += 1
    return [num for num in range(2, limit + 1) if is_p[num]]


def prime_factors(n):
    """Return the prime factors of n as a list, e.g. 60 -> [2, 2, 3, 5]."""
    if n < 2:
        raise ValueError("Number must be 2 or more.")
    factors = []
    divisor = 2
    while divisor * divisor <= n:
        while n % divisor == 0:
            factors.append(divisor)
            n = n // divisor
        divisor += 1
    if n > 1:
        factors.append(n)      # what is left over is a prime
    return factors


def power(base, exponent, modulus=None):
    """Raise base to a large power quickly (square-and-multiply).
    Takes about log2(exponent) steps instead of `exponent` steps."""
    if exponent < 0:
        raise ValueError("Exponent must not be negative.")
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = result * base
            if modulus:
                result %= modulus
        base = base * base
        if modulus:
            base %= modulus
        exponent = exponent // 2
    return result


def _fib_pair(n):
    """Helper: returns (F(n), F(n+1)) using the 'fast doubling' idea."""
    if n == 0:
        return 0, 1
    a, b = _fib_pair(n // 2)
    c = a * (2 * b - a)        # F(2k)
    d = a * a + b * b          # F(2k+1)
    if n % 2 == 0:
        return c, d
    return d, c + d


def nth_fibonacci(n):
    """nth Fibonacci number with F(0)=0, F(1)=1 (fast, works for big n)."""
    if n < 0:
        raise ValueError("n must not be negative.")
    return _fib_pair(n)[0]


def lcg_random(seed, count, low, high):
    """Pseudo-random numbers with a Linear Congruential Generator:
    next = (a * current + c) mod m. Same seed gives the same numbers."""
    if low > high:
        raise ValueError("Low must not be greater than high.")
    if count < 0:
        raise ValueError("Count must not be negative.")
    a, c, m = 1103515245, 12345, 2 ** 31
    x = seed
    numbers = []
    for _ in range(count):
        x = (a * x + c) % m
        numbers.append(low + x % (high - low + 1))
    return numbers
