"""
history.py
----------
Keeps a dictionary-based log of what the user did in this session
and sets up a log file for debugging.
"""
import logging

LOG_FILE = "algorithm_explorer.log"


def setup_logging():
    """Send log messages to a file (not the screen) so the menu stays clean."""
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )


class SessionHistory:
    """Remembers how many times each feature was used and the quiz scores."""

    def __init__(self):
        self.action_counts = {}    # {"Factorial": 2, "GCD": 1, ...}
        self.quiz_scores = []      # [(score, total), ...]

    def record_action(self, name):
        self.action_counts[name] = self.action_counts.get(name, 0) + 1

    def record_quiz(self, score, total):
        self.quiz_scores.append((score, total))

    def best_quiz_score(self):
        """Return the best (score, total) tuple, or None if no quiz taken."""
        if not self.quiz_scores:
            return None
        return max(self.quiz_scores, key=lambda pair: pair[0] / pair[1])

    def summary(self):
        """Return the history as printable text."""
        lines = ["Features used:"]
        if not self.action_counts:
            lines.append("  (nothing yet)")
        for name, count in self.action_counts.items():
            lines.append(f"  - {name}: {count} time(s)")
        lines.append("Quiz attempts:")
        if not self.quiz_scores:
            lines.append("  (none yet)")
        for number, (score, total) in enumerate(self.quiz_scores, start=1):
            lines.append(f"  Attempt {number}: {score}/{total}")
        return "\n".join(lines)
