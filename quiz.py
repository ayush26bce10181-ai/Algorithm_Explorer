"""
quiz.py
-------
Practice quiz module: makes random questions using the algorithm
functions, checks the user's answers and reports a score.
"""
import random

import array_techniques as at
import factoring_methods as fm
import number_algorithms as na

QUESTION_TYPES = ["gcd", "factorial", "prime", "binary", "fibonacci", "reverse", "kth"]


def generate_question(rng=random):
    """Return (question_text, correct_answer_as_text)."""
    kind = rng.choice(QUESTION_TYPES)

    if kind == "gcd":
        a, b = rng.randint(10, 99), rng.randint(10, 99)
        return f"What is the GCD of {a} and {b}?", str(fm.gcd(a, b))

    if kind == "factorial":
        n = rng.randint(3, 8)
        return f"What is {n}! ?", str(na.factorial(n))

    if kind == "prime":
        n = rng.randint(10, 99)
        answer = "yes" if fm.is_prime(n) else "no"
        return f"Is {n} a prime number? (yes/no)", answer

    if kind == "binary":
        n = rng.randint(5, 63)
        return f"Convert {n} to binary.", na.convert_base(n, 2)

    if kind == "fibonacci":
        n = rng.randint(6, 15)
        return (f"What is the {na.ordinal(n)} Fibonacci number? (F0=0, F1=1)",
                str(fm.nth_fibonacci(n)))

    if kind == "reverse":
        n = rng.randint(100, 99999)
        return f"Reverse the digits of {n}.", str(na.reverse_number(n))

    # kind == "kth"
    numbers = rng.sample(range(1, 50), 6)
    k = rng.randint(1, 6)
    return (f"In the list {numbers}, what is the {na.ordinal(k)} smallest number?",
            str(at.kth_smallest(numbers, k)))


def check_answer(user_answer, correct_answer):
    """Compare answers, ignoring spaces/case and accepting y/n for yes/no."""
    user = user_answer.strip().lower()
    if user == "y":
        user = "yes"
    elif user == "n":
        user = "no"
    return user == correct_answer.lower()


def run_quiz(history, num_questions=5, input_func=input, rng=random):
    """Ask `num_questions` questions, print feedback and return the score."""
    print(f"\nQuiz time! {num_questions} questions. Good luck!\n")
    score = 0
    for number in range(1, num_questions + 1):
        question, correct = generate_question(rng)
        answer = input_func(f"Q{number}. {question}\n   Your answer: ")
        if check_answer(answer, correct):
            print("   Correct!\n")
            score += 1
        else:
            print(f"   Not quite. The answer is {correct}.\n")
    print(f"Your score: {score}/{num_questions}")
    history.record_quiz(score, num_questions)
    return score
