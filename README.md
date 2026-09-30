# Algorithm Explorer

A menu-driven Python program that teaches basic problem-solving algorithms
by running them and showing the steps. Built for **CSE1021 - Introduction to
Problem Solving and Programming**.

## Overview
Instead of just giving an answer, Algorithm Explorer shows *how* an algorithm
gets there (for example, each division in Euclid's GCD algorithm). It covers
Units 3-5 of the syllabus and ends with a quiz so you can test yourself.

## Features
- **Number Algorithms:** factorial, Fibonacci series, reverse a number, base conversion (2-16), swap values, digit count/sum, character-to-number
- **Factoring Methods:** GCD and LCM (with steps), prime check, sieve of primes, prime factors, Newton's square root, fast power, fast nth Fibonacci, pseudo-random numbers
- **Arrays and Collections:** reverse, count, min/max (tuple), remove duplicates, partition, k-th smallest, set operations, word frequency (dictionary)
- **Practice Quiz:** 5 random questions with scoring
- **Session History:** shows what you used and your quiz scores
- **Safe input:** invalid input gives a friendly message instead of a crash
- **Logging:** activity saved to `algorithm_explorer.log`

## Technologies Used
- Python 3.8+ (standard library only, no installs needed)
- `unittest` for testing, `logging` for the log file
- Git and GitHub for version control
- Raptor for the flowchart

## Project Structure
```
algorithm-explorer/
├── main.py                 # menus and program flow
├── number_algorithms.py    # Unit 3 algorithms
├── factoring_methods.py    # Unit 4 algorithms
├── array_techniques.py     # Unit 5 lists, sets, dictionaries
├── quiz.py                 # quiz generation and scoring
├── validators.py           # input checking
├── history.py              # session history and logging setup
├── tests/                  # unit tests
├── docs/                   # diagrams for the report
├── statement.md
└── README.md
```

## How to Install and Run
```bash
git clone https://github.com/<your-username>/algorithm-explorer.git
cd algorithm-explorer
python main.py
```
Use the number keys to pick options and `0` to go back or exit.

## How to Run the Tests
```bash
python -m unittest discover tests
```
All tests should show `OK`.

## Sample Output
```
=== FACTORING METHODS ===
Choose an option: 1
First number: 48
Second number: 18
Euclid's algorithm steps:
   48 = 2 x 18 + 12
   18 = 1 x 12 + 6
   12 = 2 x 6 + 0
GCD = 6
LCM = 144
```

## Screenshots
_Add screenshots of the main menu, a GCD run and the quiz here._

## Author
Your Name - Reg. No. - VIT
