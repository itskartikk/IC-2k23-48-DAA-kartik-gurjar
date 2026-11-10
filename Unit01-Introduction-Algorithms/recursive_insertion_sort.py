"""
Insertion Sort (recursive)
--------------------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    To sort the first n items: first sort the first n-1 items (the
    recursive call), then insert item n into that sorted part.

    Base case: one item is already sorted.

    The order matters. The recursive call comes FIRST, so the function
    dives down to n = 1 and the inserting happens on the way back up.

Recurrence
    T(n) = T(n-1) + O(n)    which solves to O(n^2)

Complexity
    Best    O(n)      each insert stops after one comparison
    Average O(n^2)
    Worst   O(n^2)
    Space   O(n)      recursion stack, against O(1) for the loop version
"""


def recursive_insertion_sort(values, n=None, show_steps=False):
    """Sort the first n items of `values` in place."""
    if n is None:
        n = len(values)

    # Base case.
    if n <= 1:
        return

    # Sort the first n-1 items.
    recursive_insertion_sort(values, n - 1, show_steps)

    # Insert the nth item into the sorted first n-1.
    key = values[n - 1]
    j = n - 2
    while j >= 0 and values[j] > key:
        values[j + 1] = values[j]
        j -= 1
    values[j + 1] = key

    if show_steps:
        print(f"    returning from n = {n}: inserted {key:>3} -> {values[:n]}")


def main():
    print("=" * 64)
    print("  INSERTION SORT (recursive)")
    print("=" * 64)

    data = [38, 27, 43, 3, 9, 82, 10]
    print(f"\n  Input : {data}\n")
    print("  The calls go down to n = 1 first. The work below is printed")
    print("  as each call returns:\n")
    recursive_insertion_sort(data, show_steps=True)
    print(f"\n  Output: {data}")

    print("\n  Recurrence: T(n) = T(n-1) + O(n)  =>  O(n^2)")
    print(f"  Stack depth for {len(data)} items: {len(data)} frames, so O(n) space.")
    print("=" * 64)


if __name__ == "__main__":
    main()
