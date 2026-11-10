"""
Bubble Sort (iterative)
-----------------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    Walk through the list comparing each pair of neighbours and swap
    them if they are in the wrong order. After one full pass the
    largest value has "bubbled" to the end, so the next pass can stop
    one position earlier.

Optimisation
    If a whole pass makes no swap, the list is already sorted and the
    function stops. That makes the best case (sorted input) O(n)
    instead of O(n^2).

Complexity
    Best    O(n)      already sorted, one pass and no swaps
    Average O(n^2)
    Worst   O(n^2)    reverse sorted
    Space   O(1)      sorts in place
    Stable  yes       equal values never swap past each other
"""


def bubble_sort(values, show_passes=False):
    """Sort `values` in place. Returns (comparisons, swaps, passes)."""
    n = len(values)
    comparisons = swaps = passes = 0

    for done in range(n - 1):
        swapped = False
        passes += 1

        # The last `done` items are already in their final place.
        for j in range(n - 1 - done):
            comparisons += 1
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swaps += 1
                swapped = True

        if show_passes:
            print(f"    after pass {passes}: {values}")

        if not swapped:
            break  # nothing moved, so the list is sorted

    return comparisons, swaps, passes


def main():
    print("=" * 60)
    print("  BUBBLE SORT (iterative)")
    print("=" * 60)

    data = [29, 10, 14, 37, 13, 5, 42, 8]
    print(f"\n  Input : {data}\n")
    comparisons, swaps, passes = bubble_sort(data, show_passes=True)
    print(f"\n  Output: {data}")
    print(f"  Passes = {passes}, comparisons = {comparisons}, swaps = {swaps}")

    print("\n  --- Effect of the early exit on 8 items ---\n")
    cases = {
        "already sorted": [1, 2, 3, 4, 5, 6, 7, 8],
        "reverse sorted": [8, 7, 6, 5, 4, 3, 2, 1],
        "one item out of place": [1, 2, 3, 5, 4, 6, 7, 8],
    }
    print(f"  {'Case':<24}{'Passes':>8}{'Comparisons':>14}{'Swaps':>8}")
    print("  " + "-" * 54)
    for name, case in cases.items():
        comparisons, swaps, passes = bubble_sort(case)
        print(f"  {name:<24}{passes:>8}{comparisons:>14}{swaps:>8}")

    print("\n  Sorted input needs one pass of n-1 = 7 comparisons: O(n).")
    print("  Reverse input needs n(n-1)/2 = 28 comparisons: O(n^2).")
    print("=" * 60)


if __name__ == "__main__":
    main()
