"""
Linear Search
-------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Idea
    Check every item from the start until the target is found or the
    list ends. It needs nothing from the data: the list does not have
    to be sorted.

Complexity
    Best    O(1)      target is the first item
    Average O(n)      about n/2 comparisons when the target is present
    Worst   O(n)      target is last, or not there at all
    Space   O(1)
"""


def linear_search(values, target):
    """Return (index, comparisons). Index is -1 when not found."""
    comparisons = 0
    for index, value in enumerate(values):
        comparisons += 1
        if value == target:
            return index, comparisons
    return -1, comparisons


def main():
    print("=" * 58)
    print("  LINEAR SEARCH")
    print("=" * 58)

    data = [42, 17, 8, 93, 56, 21, 70, 35, 4, 68]
    print(f"\n  List ({len(data)} items, unsorted): {data}\n")

    print(f"  {'Target':<10}{'Result':<22}{'Comparisons':>12}  Case")
    print("  " + "-" * 54)
    for target, case in [(42, "best"), (56, "average"),
                         (68, "worst, found"), (99, "worst, absent")]:
        index, comparisons = linear_search(data, target)
        result = f"found at index {index}" if index != -1 else "not found"
        print(f"  {target:<10}{result:<22}{comparisons:>12}  {case}")

    # Average over every possible successful search.
    total = sum(linear_search(data, value)[1] for value in data)
    print(f"\n  Average comparisons over all {len(data)} successful searches: "
          f"{total / len(data):.1f}")
    print(f"  Formula (n + 1) / 2 = {(len(data) + 1) / 2:.1f}")
    print("=" * 58)


if __name__ == "__main__":
    main()
