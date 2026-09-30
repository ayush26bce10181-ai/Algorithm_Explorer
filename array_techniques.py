"""
array_techniques.py
-------------------
Array and collection techniques from Unit 5 of CSE1021:
reversal, counting, maximum, duplicate removal, partitioning,
k-th smallest, tuples, sets and dictionaries.
"""


def reverse_array(arr):
    """Return a reversed copy of a list by swapping the two ends."""
    result = list(arr)
    left, right = 0, len(result) - 1
    while left < right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1
    return result


def count_occurrences(arr, target):
    """Count how many times `target` appears in the list."""
    count = 0
    for item in arr:
        if item == target:
            count += 1
    return count


def find_maximum(arr):
    """Find the biggest number in a list."""
    if not arr:
        raise ValueError("The list is empty.")
    biggest = arr[0]
    for item in arr:
        if item > biggest:
            biggest = item
    return biggest


def find_minimum(arr):
    """Find the smallest number in a list."""
    if not arr:
        raise ValueError("The list is empty.")
    smallest = arr[0]
    for item in arr:
        if item < smallest:
            smallest = item
    return smallest


def min_max(arr):
    """Return (minimum, maximum) as a tuple."""
    return find_minimum(arr), find_maximum(arr)


def remove_duplicates_sorted(arr):
    """Remove duplicates from a SORTED list (equal items sit together)."""
    if not arr:
        return []
    unique = [arr[0]]
    for item in arr[1:]:
        if item != unique[-1]:
            unique.append(item)
    return unique


def partition_array(arr, pivot):
    """Split a list into (smaller, equal, larger) compared to the pivot."""
    smaller, equal, larger = [], [], []
    for item in arr:
        if item < pivot:
            smaller.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            larger.append(item)
    return smaller, equal, larger


def kth_smallest(arr, k):
    """Find the k-th smallest element (k=1 means the smallest).
    Uses partitioning, so the whole list never needs to be sorted."""
    if not arr:
        raise ValueError("The list is empty.")
    if k < 1 or k > len(arr):
        raise ValueError(f"k must be between 1 and {len(arr)}.")
    pivot = arr[len(arr) // 2]
    smaller, equal, larger = partition_array(arr, pivot)
    if k <= len(smaller):
        return kth_smallest(smaller, k)
    if k <= len(smaller) + len(equal):
        return pivot
    return kth_smallest(larger, k - len(smaller) - len(equal))


def set_operations(list_a, list_b):
    """Return a dictionary holding the common set operations."""
    a, b = set(list_a), set(list_b)
    return {
        "union": sorted(a | b),
        "intersection": sorted(a & b),
        "only in first": sorted(a - b),
        "only in second": sorted(b - a),
        "in one but not both": sorted(a ^ b),
    }


def word_frequency(text):
    """Count how often each word appears (dictionary example)."""
    counts = {}
    for word in text.lower().split():
        word = word.strip(".,!?;:\"'()")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts
