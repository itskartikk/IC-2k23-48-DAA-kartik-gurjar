"""
Selection Sort
--------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    Find the smallest value in the unsorted part and swap it into the
    first unsorted position. Repeat for the next position.

Complexity
    Best    O(n^2)    it always scans the whole unsorted part, so
    Average O(n^2)    sorted input gains nothing
    Worst   O(n^2)
    Space   O(1)
    Stable  no        the long-distance swap can carry a value past
                      an equal one (demonstrated below)

Its one advantage
    At most n-1 swaps, the fewest of the three simple sorts. That
    matters when writing to memory is expensive.
"""


def selection_sort(values, show_steps=False):
    """Sort `values` in place. Returns (comparisons, swaps)."""
    n = len(values)
    comparisons = swaps = 0

    for i in range(n - 1):
        smallest = i

        for j in range(i + 1, n):
            comparisons += 1
            if values[j] < values[smallest]:
                smallest = j

        if smallest != i:
            values[i], values[smallest] = values[smallest], values[i]
            swaps += 1

        if show_steps:
            print(f"    position {i}: smallest is {values[i]:>3} -> {values}")

    return comparisons, swaps


def main():
    print("=" * 62)
    print("  SELECTION SORT")
    print("=" * 62)

    data = [64, 25, 12, 22, 11, 90, 5]
    print(f"\n  Input : {data}\n")
    comparisons, swaps = selection_sort(data, show_steps=True)
    print(f"\n  Output: {data}")
    print(f"  Comparisons = {comparisons}, swaps = {swaps}")

    print("\n  --- Comparisons do not depend on the input, 8 items ---\n")
    print(f"  {'Case':<18}{'Comparisons':>13}{'Swaps':>8}")
    print("  " + "-" * 39)
    for name, case in [("already sorted", list(range(1, 9))),
                       ("reverse sorted", list(range(8, 0, -1))),
                       ("mixed", [5, 2, 8, 1, 7, 3, 6, 4])]:
        comparisons, swaps = selection_sort(case)
        print(f"  {name:<18}{comparisons:>13}{swaps:>8}")
    print("\n  Always n(n-1)/2 = 28 comparisons, but never more than 7 swaps.")

    print("\n  --- Why it is not stable ---\n")
    # Pairs sorted by number only. Letters mark the original order.
    cards = [(4, "a"), (4, "b"), (1, "c")]
    print(f"  Before: {cards}")
    n = len(cards)
    for i in range(n - 1):
        smallest = i
        for j in range(i + 1, n):
            if cards[j][0] < cards[smallest][0]:
                smallest = j
        cards[i], cards[smallest] = cards[smallest], cards[i]
    print(f"  After : {cards}")
    print("  (4, 'a') started before (4, 'b') and ended after it.")
    print("=" * 62)


if __name__ == "__main__":
    main()
