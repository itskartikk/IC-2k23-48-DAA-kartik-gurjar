"""
Binary Search (iterative)
-------------------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    Works only on a SORTED list. Look at the middle item. If it is the
    target, stop. If the target is smaller, it can only be in the left
    half; if larger, only in the right half. Either way half of the
    list is thrown away with one comparison.

Complexity
    Best    O(1)        target is the middle item
    Average O(log n)
    Worst   O(log n)    at most floor(log2 n) + 1 probes
    Space   O(1)        just two index variables

    A million items need at most 20 probes. Linear search would need
    up to a million.
"""


def binary_search(values, target, show_steps=False):
    """Return (index, probes). Index is -1 when not found."""
    low, high = 0, len(values) - 1
    probes = 0

    while low <= high:
        middle = (low + high) // 2
        probes += 1

        if show_steps:
            print(f"    probe {probes}: low={low:<2} high={high:<2} "
                  f"middle={middle:<2} value={values[middle]}")

        if values[middle] == target:
            return middle, probes
        if values[middle] < target:
            low = middle + 1       # target can only be to the right
        else:
            high = middle - 1      # target can only be to the left

    return -1, probes


def main():
    print("=" * 58)
    print("  BINARY SEARCH (iterative)")
    print("=" * 58)

    data = [3, 8, 12, 17, 21, 29, 35, 42, 56, 68, 70, 84, 93]
    print(f"\n  Sorted list ({len(data)} items): {data}")

    for target in (70, 5):
        print(f"\n  Searching for {target}:")
        index, probes = binary_search(data, target, show_steps=True)
        if index != -1:
            print(f"  Found at index {index} after {probes} probes.")
        else:
            print(f"  Not found after {probes} probes.")

    print("\n  --- Worst case probes as the list grows ---\n")
    print(f"  {'Items':>12}{'Binary search':>16}{'Linear search':>16}")
    print("  " + "-" * 44)
    for size in (10, 100, 1_000, 100_000, 1_000_000):
        big = list(range(size))
        # A value larger than everything forces the longest search.
        _, probes = binary_search(big, size)
        print(f"  {size:>12,}{probes:>16}{size:>16,}")
    print("=" * 58)


if __name__ == "__main__":
    main()
