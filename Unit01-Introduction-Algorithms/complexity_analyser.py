"""
Complexity Analyser
-------------------
Author : Kartik Gurjar (IC-2K23-48)
Unit   : 1 - Introduction to Algorithms

Purpose
    Measure the algorithms in this unit instead of just quoting their
    Big-O. Each one is timed on growing inputs and the results are
    checked against the theory.

The check used: the doubling test
    Double the input size and see what happens to the running time.

        time x2   -> O(n)
        time x4   -> O(n^2)
        no change -> O(log n), near enough

    The ratio is printed next to every timing so the growth rate can be
    read off directly.

Fairness
    Every sort gets its own copy of the same random list, and each
    timing is the best of several runs, which filters out interference
    from other programs.

Output
    Tables on screen, and complexity_plot.png if matplotlib is
    installed (pip install matplotlib). The program still runs
    without it.
"""

import os
import random
import sys
import time

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from iterative_binary_search import binary_search as iterative_binary_search
from linear_search import linear_search
from recursive_binary_search import binary_search as recursive_binary_search
from recursive_bubble_sort import recursive_bubble_sort
from recursive_insertion_sort import recursive_insertion_sort
from selection_sort import selection_sort

# The recursive sorts go one stack frame deep per item.
sys.setrecursionlimit(10_000)

SORT_SIZES = [100, 200, 400, 800, 1600]
SEARCH_SIZES = [1_000, 10_000, 100_000, 1_000_000]
REPEATS = 3

SORTS = {
    "Bubble": bubble_sort,
    "Bubble (recursive)": recursive_bubble_sort,
    "Insertion": insertion_sort,
    "Insertion (recursive)": recursive_insertion_sort,
    "Selection": selection_sort,
}


def best_time(function, make_input, repeats=REPEATS):
    """Smallest time, in seconds, over several runs on fresh input."""
    best = float("inf")
    for _ in range(repeats):
        data = make_input()
        start = time.perf_counter()
        function(data)
        best = min(best, time.perf_counter() - start)
    return best


def time_sorts(make_list):
    """Time every sort at every size. Returns {name: [seconds, ...]}."""
    results = {name: [] for name in SORTS}
    for size in SORT_SIZES:
        base = make_list(size)
        for name, sort in SORTS.items():
            results[name].append(best_time(sort, lambda: list(base)))
    return results


def print_sort_table(title, results):
    print(f"\n  {title}\n")
    header = f"  {'Algorithm':<24}" + "".join(f"{f'n={size}':>12}" for size in SORT_SIZES)
    print(header + f"{'ratio':>9}")
    print("  " + "-" * (len(header) + 7))
    for name, times in results.items():
        cells = "".join(f"{seconds * 1000:>10.2f}ms" for seconds in times)
        # How much slower the largest size is than the one before it.
        ratio = times[-1] / times[-2] if times[-2] > 0 else float("nan")
        print(f"  {name:<24}{cells}{ratio:>8.1f}x")


def time_searches():
    """Worst case searches: the target is absent."""
    rows = []
    for size in SEARCH_SIZES:
        data = list(range(size))
        target = size  # larger than everything, so never found

        linear = best_time(lambda values: linear_search(values, target), lambda: data)

        # Binary search is too fast to time once, so time many calls.
        calls = 2000
        start = time.perf_counter()
        for _ in range(calls):
            iterative_binary_search(data, target)
        iterative = (time.perf_counter() - start) / calls

        start = time.perf_counter()
        for _ in range(calls):
            recursive_binary_search(data, target)
        recursive = (time.perf_counter() - start) / calls

        _, linear_steps = linear_search(data, target)
        _, binary_steps = iterative_binary_search(data, target)
        rows.append((size, linear, iterative, recursive, linear_steps, binary_steps))
    return rows


def save_plot(random_results, search_rows, path):
    """Draw the two charts. Returns False if matplotlib is missing."""
    try:
        import matplotlib
        matplotlib.use("Agg")  # draw to a file, no window needed
        import matplotlib.pyplot as plt
    except ImportError:
        return False

    figure, (left, right) = plt.subplots(1, 2, figsize=(13, 5))

    for name, times in random_results.items():
        left.plot(SORT_SIZES, [t * 1000 for t in times], marker="o", label=name)
    left.set_title("Sorting on random input")
    left.set_xlabel("Number of items (n)")
    left.set_ylabel("Time (milliseconds)")
    left.legend()
    left.grid(alpha=0.3)

    sizes = [row[0] for row in search_rows]
    right.plot(sizes, [row[4] for row in search_rows], marker="o", label="Linear search")
    right.plot(sizes, [row[5] for row in search_rows], marker="o", label="Binary search")
    right.set_xscale("log")
    right.set_yscale("log")
    right.set_title("Searching, worst case comparisons")
    right.set_xlabel("Number of items (n), log scale")
    right.set_ylabel("Comparisons, log scale")
    right.legend()
    right.grid(alpha=0.3)

    figure.suptitle("Unit 1 - measured growth of sorting and searching")
    figure.tight_layout()
    figure.savefig(path, dpi=120)
    plt.close(figure)
    return True


def main():
    random.seed(48)  # same lists on every run, so results are repeatable

    print("=" * 96)
    print("  COMPLEXITY ANALYSER")
    print("=" * 96)
    print("\n  Timing each algorithm (best of "
          f"{REPEATS} runs). This takes a few seconds...")

    random_results = time_sorts(lambda n: [random.randint(0, 10 * n) for _ in range(n)])
    sorted_results = time_sorts(lambda n: list(range(n)))
    reverse_results = time_sorts(lambda n: list(range(n, 0, -1)))

    print("\n" + "-" * 96)
    print("  PART 1: SORTING")
    print("  'ratio' = time at n=1600 divided by time at n=800.")
    print("  About 4x means O(n^2). About 2x means O(n).")
    print("-" * 96)

    print_sort_table("Random input (average case)", random_results)
    print_sort_table("Already sorted input (best case)", sorted_results)
    print_sort_table("Reverse sorted input (worst case)", reverse_results)

    print("\n  What the numbers show")
    print("    - Random and reverse input: every sort is near 4x, as O(n^2) predicts.")
    print("    - Sorted input: bubble and insertion drop to about 2x, their O(n)")
    print("      best case. Selection stays near 4x because it always scans")
    print("      everything.")
    print("    - The loop versions here also count their comparisons, which costs")
    print("      a little time, so compare growth rates, not who wins by a few ms.")

    print("\n" + "-" * 96)
    print("  PART 2: SEARCHING (worst case: the target is not in the list)")
    print("-" * 96 + "\n")

    search_rows = time_searches()
    print(f"  {'n':>11}{'Linear':>13}{'Binary (iter)':>16}{'Binary (rec)':>15}"
          f"{'Linear steps':>15}{'Binary steps':>14}")
    print("  " + "-" * 84)
    for size, linear, iterative, recursive, linear_steps, binary_steps in search_rows:
        print(f"  {size:>11,}{linear * 1000:>11.3f}ms{iterative * 1e6:>14.2f}us"
              f"{recursive * 1e6:>13.2f}us{linear_steps:>15,}{binary_steps:>14}")

    print("\n  What the numbers show")
    print("    - Linear search grows 10x each time n grows 10x: O(n).")
    print("    - Binary search adds only 3 or 4 steps per 10x: O(log n).")
    print("    - The recursive version is a little slower than the iterative")
    print("      one. Same number of steps, plus the cost of function calls.")
    print("    - Binary search needs sorted data. Linear search does not.")

    plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "complexity_plot.png")
    print()
    if save_plot(random_results, search_rows, plot_path):
        print(f"  Chart saved to {os.path.basename(plot_path)}")
    else:
        print("  matplotlib is not installed, so no chart was drawn.")
        print("  Install it with: pip install matplotlib")

    print("\n  Note: the times depend on the machine. The ratios are what matter.")
    print("=" * 96)


if __name__ == "__main__":
    main()
