"""
Insertion Sort (iterative)
--------------------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    The way most people sort playing cards in their hand. The left part
    of the list is kept sorted. Take the next value (the "key"), shift
    every larger value in the sorted part one place to the right, and
    drop the key into the gap.

Complexity
    Best    O(n)      sorted input: each key is compared once, no shifts
    Average O(n^2)
    Worst   O(n^2)    reverse sorted: every key travels to the front
    Space   O(1)
    Stable  yes

Why it matters
    On small or nearly sorted input it beats the O(n log n) sorts,
    which is why library sorts such as Timsort use it for short runs.
"""


def insertion_sort(values, show_steps=False):
    """Sort `values` in place. Returns (comparisons, shifts)."""
    comparisons = shifts = 0

    for i in range(1, len(values)):
        key = values[i]
        j = i - 1

        # Shift larger values right until the key's place is found.
        while j >= 0:
            comparisons += 1
            if values[j] <= key:
                break
            values[j + 1] = values[j]
            shifts += 1
            j -= 1

        values[j + 1] = key

        if show_steps:
            sorted_part = values[:i + 1]
            rest = values[i + 1:]
            print(f"    insert {key:>3}: {sorted_part} | {rest}")

    return comparisons, shifts


def main():
    print("=" * 62)
    print("  INSERTION SORT (iterative)")
    print("=" * 62)

    data = [31, 41, 59, 26, 53, 58, 97, 12]
    print(f"\n  Input : {data}")
    print("  (sorted part | unsorted part)\n")
    comparisons, shifts = insertion_sort(data, show_steps=True)
    print(f"\n  Output: {data}")
    print(f"  Comparisons = {comparisons}, shifts = {shifts}")

    print("\n  --- Best case against worst case, 8 items ---\n")
    print(f"  {'Case':<18}{'Comparisons':>13}{'Shifts':>9}")
    print("  " + "-" * 40)
    for name, case in [("already sorted", list(range(1, 9))),
                       ("reverse sorted", list(range(8, 0, -1)))]:
        comparisons, shifts = insertion_sort(case)
        print(f"  {name:<18}{comparisons:>13}{shifts:>9}")

    print("\n  Sorted input: n-1 = 7 comparisons and nothing moves.")
    print("  Reverse input: n(n-1)/2 = 28 of each.")
    print("=" * 62)


if __name__ == "__main__":
    main()
