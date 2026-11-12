import time
import random
import sys
import matplotlib.pyplot as plt
import numpy as np

# Increase recursion depth to prevent crashes during recursive sorts
sys.setrecursionlimit(25000)

# ==========================================
# 1. ALGORITHM IMPLEMENTATIONS
# ==========================================

# --- SORTING ALGORITHMS ---

def recursive_insertion_sort(arr, i=1, j=None):
    if i >= len(arr): return arr
    if j is None: j = i
    if j > 0 and arr[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
        return recursive_insertion_sort(arr, i, j - 1)
    return recursive_insertion_sort(arr, i + 1, None)

def insertion_sort(arr):
    # Adapted to standard in-place for fair benchmarking
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def recursive_bubble_sort(arr, n, i):
    if n <= 1: return arr
    if i == n - 1:
        return recursive_bubble_sort(arr, n - 1, 0)
    if arr[i] > arr[i + 1]:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return recursive_bubble_sort(arr, n, i + 1)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# --- SEARCHING ALGORITHMS ---

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

def binary_search(lst, tar):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = (start + end) // 2
        if tar == lst[mid]: return mid
        elif tar < lst[mid]: end = mid - 1
        else: start = mid + 1
    return -1

def recursive_binary_search(lst, a, start, end):
    if start > end: return -1
    mid = (start + end) // 2
    if a == lst[mid]: return mid
    elif a < lst[mid]: return recursive_binary_search(lst, a, start, mid - 1)
    else: return recursive_binary_search(lst, a, mid + 1, end)


# ==========================================
# 2. BENCHMARKING ENGINE
# ==========================================

def measure_time(func, *args):
    """Measures the execution time of a function."""
    start = time.perf_counter()
    func(*args)
    return time.perf_counter() - start

def run_benchmarks():
    # Define test sizes (calibrated to stay within safe recursion limits for recursive O(N^2) implementations)
    sort_sizes = [20, 40, 60, 80, 100, 120, 140]
    search_sizes = [1000, 5000, 10000, 50000, 100000]
    
    results = {
        "Insertion Sort (Iterative)": [], "Insertion Sort (Recursive)": [],
        "Bubble Sort (Iterative)": [], "Bubble Sort (Recursive)": [],
        "Selection Sort": [], 
        "Linear Search": [], "Binary Search (Iterative)": [], "Binary Search (Recursive)": []
    }

    print("Running Sort Benchmarks...")
    for n in sort_sizes:
        arr = [random.randint(0, 10000) for _ in range(n)]
        
        # Test sorting algorithms (using copies of the array)
        results["Insertion Sort (Iterative)"].append(measure_time(insertion_sort, arr.copy()))
        results["Insertion Sort (Recursive)"].append(measure_time(recursive_insertion_sort, arr.copy()))
        results["Bubble Sort (Iterative)"].append(measure_time(bubble_sort, arr.copy()))
        results["Bubble Sort (Recursive)"].append(measure_time(recursive_bubble_sort, arr.copy(), n, 0))
        results["Selection Sort"].append(measure_time(selection_sort, arr.copy()))

    print("Running Search Benchmarks...")
    for n in search_sizes:
        arr = list(range(n))  # Sorted array for search algorithms
        target = -1           # Worst-case scenario (not found)
        
        results["Linear Search"].append(measure_time(linear_search, arr, target))
        results["Binary Search (Iterative)"].append(measure_time(binary_search, arr, target))
        results["Binary Search (Recursive)"].append(measure_time(recursive_binary_search, arr, target, 0, n - 1))

    return sort_sizes, search_sizes, results

# ==========================================
# 3. VISUALIZATION & ANALYSIS
# ==========================================

def plot_results(sort_sizes, search_sizes, results):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Sorting Algorithms O(N^2)
    ax1.plot(sort_sizes, results["Bubble Sort (Iterative)"], label='Bubble Sort (Iter)', marker='o')
    ax1.plot(sort_sizes, results["Bubble Sort (Recursive)"], label='Bubble Sort (Rec)', marker='s')
    ax1.plot(sort_sizes, results["Selection Sort"], label='Selection Sort', marker='^')
    ax1.plot(sort_sizes, results["Insertion Sort (Iterative)"], label='Insertion Sort (Iter)', marker='x')
    ax1.plot(sort_sizes, results["Insertion Sort (Recursive)"], label='Insertion Sort (Rec)', marker='d')
    
    # Plot theoretical O(N^2) line for reference (scaled down for visualization)
    theoretical_n2 = [((n**2) / (sort_sizes[-1]**2)) * max(results["Bubble Sort (Iterative)"]) for n in sort_sizes]
    ax1.plot(sort_sizes, theoretical_n2, '--', color='gray', label='Theoretical O(N²)')
    
    ax1.set_title("Sorting Algorithms (Experimental vs Theoretical O(N²))")
    ax1.set_xlabel("Input Size (N)")
    ax1.set_ylabel("Time (seconds)")
    ax1.legend()
    ax1.grid(True)

    # Plot 2: Searching Algorithms O(N) vs O(log N)
    ax2.plot(search_sizes, results["Linear Search"], label='Linear Search (Iter)', marker='o', color='red')
    ax2.plot(search_sizes, results["Binary Search (Iterative)"], label='Binary Search (Iter)', marker='^', color='green')
    ax2.plot(search_sizes, results["Binary Search (Recursive)"], label='Binary Search (Rec)', marker='x', color='blue')
    
    # Plot theoretical O(N) and O(log N)
    theoretical_n = [(n / search_sizes[-1]) * max(results["Linear Search"]) for n in search_sizes]
    ax2.plot(search_sizes, theoretical_n, '--', color='pink', label='Theoretical O(N)')
    
    ax2.set_title("Searching Algorithms (O(N) vs O(log N))")
    ax2.set_xlabel("Input Size (N)")
    ax2.set_ylabel("Time (seconds)")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

# Run the analyzer
if __name__ == "__main__":
    sort_sizes, search_sizes, results = run_benchmarks()
    plot_results(sort_sizes, search_sizes, results)