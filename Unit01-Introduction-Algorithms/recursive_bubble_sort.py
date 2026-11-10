"""
Bubble Sort (recursive)
-----------------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    The same algorithm as the iterative version, with the outer loop
    replaced by recursion. One call does one pass over the first n
    items, which puts the largest of them at position n-1. The function
    then calls itself on the first n-1 items.

    Base case: a list of 0 or 1 items is already sorted. The early exit
    is kept as well: if a pass makes no swap, the recursion stops.

Recurrence
    T(n) = T(n-1) + (n-1)   which solves to O(n^2)

Complexity
    Best    O(n)      sorted input, one pass and stop
    Average O(n^2)
    Worst   O(n^2)
    Space   O(n)      one stack frame per pass, unlike the O(1)
                      iterative version. That stack is the real cost
                      of writing it recursively: Python's default
                      recursion limit of 1000 caps the list size.
"""


def recursive_bubble_sort(values, n=None, depth=0, show_calls=False):
    """Sort the first n items of `values` in place.

    Returns the deepest recursion level reached.
    """
    if n is None:
        n = len(values)

    # Base case.
    if n <= 1:
        return depth

    # One pass: push the largest of the first n items to index n-1.
    swapped = False
    for i in range(n - 1):
        if values[i] > values[i + 1]:
            values[i], values[i + 1] = values[i + 1], values[i]
            swapped = True

    if show_calls:
        print(f"    call {depth + 1} (n = {n}): {values}")

    if not swapped:
        return depth

    # Recursive case: the last item is placed, sort the rest.
    return recursive_bubble_sort(values, n - 1, depth + 1, show_calls)


def main():
    print("=" * 60)
    print("  BUBBLE SORT (recursive)")
    print("=" * 60)

    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n  Input : {data}\n")
    depth = recursive_bubble_sort(data, show_calls=True)
    print(f"\n  Output: {data}")
    print(f"  Deepest recursion level: {depth + 1}")

    print("\n  --- Recursion depth by input ---\n")
    for name, case in [("already sorted", list(range(1, 9))),
                       ("reverse sorted", list(range(8, 0, -1)))]:
        depth = recursive_bubble_sort(case)
        print(f"  {name:<16} 8 items -> {depth + 1} call(s) deep")

    print("\n  Each pass is one stack frame, so the worst case uses O(n)")
    print("  extra memory where the iterative version uses O(1).")
    print("=" * 60)


if __name__ == "__main__":
    main()
