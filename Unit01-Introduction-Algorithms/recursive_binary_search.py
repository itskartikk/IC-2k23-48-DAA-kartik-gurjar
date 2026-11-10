"""
Binary Search (recursive)
-------------------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    The same halving as the iterative version, written as a function
    that calls itself on whichever half can still hold the target.

    Base case 1: low > high, the range is empty, so the target is absent.
    Base case 2: the middle item is the target.

Recurrence
    T(n) = T(n/2) + O(1)    which solves to O(log n)

Complexity
    Time    O(log n)
    Space   O(log n)    one stack frame per halving. The iterative
                        version does the same job in O(1) space, which
                        is why it is the one used in practice.
"""


def binary_search(values, target, low=0, high=None, depth=1, show_calls=False):
    """Return (index, depth). Index is -1 when not found."""
    if high is None:
        high = len(values) - 1

    # Base case: nothing left to search.
    if low > high:
        return -1, depth - 1

    middle = (low + high) // 2

    if show_calls:
        indent = "  " * depth
        print(f"  {indent}call {depth}: search [{low}..{high}], "
              f"middle value = {values[middle]}")

    # Base case: found it.
    if values[middle] == target:
        return middle, depth

    # Recursive cases: keep only the half that can hold the target.
    if values[middle] < target:
        return binary_search(values, target, middle + 1, high, depth + 1, show_calls)
    return binary_search(values, target, low, middle - 1, depth + 1, show_calls)


def main():
    print("=" * 58)
    print("  BINARY SEARCH (recursive)")
    print("=" * 58)

    data = [2, 5, 9, 14, 18, 23, 31, 37, 44, 52, 61, 75, 88, 96, 99]
    print(f"\n  Sorted list ({len(data)} items): {data}")

    for target in (61, 15):
        print(f"\n  Searching for {target}:")
        index, depth = binary_search(data, target, show_calls=True)
        if index != -1:
            print(f"  Found at index {index}, recursion depth {depth}.")
        else:
            print(f"  Not found, recursion depth {depth}.")

    print("\n  Recurrence: T(n) = T(n/2) + O(1)  =>  O(log n)")
    print("  The indentation above is the call stack: O(log n) space.")
    print("=" * 58)


if __name__ == "__main__":
    main()
