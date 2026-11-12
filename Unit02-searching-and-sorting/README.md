# Sorting & Searching Algorithms — Python Implementation Repository

A collection of classic sorting and searching algorithms implemented in Python, covering both **iterative** and **recursive** approaches. This repository is intended as a learning resource for understanding core Data Structures & Algorithms (DSA) concepts, complexity analysis, and the trade-offs between different implementation strategies.

---

## Table of Contents

1. [Bubble Sort (Iterative)](#1-bubble-sort-iterative)
2. [Bubble Sort (Recursive)](#2-bubble-sort-recursive)
3. [Insertion Sort (Iterative)](#3-insertion-sort-iterative)
4. [Insertion Sort (Recursive)](#4-insertion-sort-recursive)
5. [Selection Sort](#5-selection-sort)
6. [Linear Search](#6-linear-search)
7. [Binary Search (Iterative)](#7-binary-search-iterative)
8. [Binary Search (Recursive)](#8-binary-search-recursive)
9. [Overall Complexity Comparison](#overall-complexity-comparison)
10. [Learning Outcomes](#learning-outcomes)
11. [How to Run](#how-to-run)

---

## 1. Bubble Sort (Iterative)

**File:** `bubble_sort.py`

### Problem Statement
Given an unsorted list of integers, sort it in ascending order by repeatedly comparing and swapping adjacent elements.

### Algorithm / Approach
- Repeatedly step through the list, comparing each pair of adjacent elements.
- Swap them if they are in the wrong order.
- After each full pass, the largest unsorted element "bubbles up" to its correct position at the end.
- A `done` flag is used to detect if any swap occurred in a pass — if not, the list is already sorted, and the algorithm exits early (optimization over the naive version).

### Pseudocode
```
for i in 0 to n-2:
    swapped = false
    for j in 0 to n-i-2:
        if lst[j] > lst[j+1]:
            swap(lst[j], lst[j+1])
            swapped = true
    if not swapped:
        break
```

### Time & Space Complexity
| Case | Time | Space |
|---|---|---|
| Best (already sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

The early-exit `done` flag gives this version O(n) best-case time, unlike the naive bubble sort which is always O(n²).

### Sample Input / Output
```
Input:  [2, 78, 4, 9, 1, 8, 5, 0]
Output: done!!! [0, 1, 2, 4, 5, 8, 9, 78]
```

---

## 2. Bubble Sort (Recursive)

**File:** `Recursive_Bubble_Sort.py`

### Problem Statement
Same as Bubble Sort above, but implemented using recursion instead of nested loops.

### Algorithm / Approach
- Recursion replaces the outer loop's shrinking boundary (`n`) and the inner loop's index (`i`).
- For a given unsorted length `n`, walk index `i` from `0` to `n-2`, comparing and swapping adjacent elements.
- When `i` reaches `n-1` (end of the current pass), recurse with a reduced boundary `n-1` and reset `i` to `0`, representing the next pass.
- Base case: when `n == 0`, the array is fully sorted.

### Pseudocode
```
function b_sort(arr, n, i):
    if n == 0: return
    if i == n-1:
        b_sort(arr, n-1, 0)   // next pass
        return
    if arr[i] > arr[i+1]:
        swap(arr[i], arr[i+1])
    return b_sort(arr, n, i+1)  // next comparison
```

### Time & Space Complexity
| Case | Time | Space |
|---|---|---|
| Best | O(n²)* | O(n) |
| Average | O(n²) | O(n) |
| Worst | O(n²) | O(n) |

*Note: unlike the iterative version, this recursive implementation has no early-exit optimization, so it always performs the full O(n²) comparisons even on an already-sorted array. Space complexity is **O(n)** due to the recursion call stack (n nested passes), whereas the iterative version uses O(1) auxiliary space.

### Sample Input / Output
```
Input:  [1, 6, 2, 8, 4, 9, 5, 7, 3]
Output: sorted List is : [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 3. Insertion Sort (Iterative)

**File:** `Insertion_Sort.py`

### Problem Statement
Sort an array by building the sorted portion one element at a time, inserting each new element into its correct position relative to the already-sorted prefix.

### Algorithm / Approach
- Treat the first element as a trivially sorted sub-array.
- For each subsequent element (`key`), shift all larger elements in the sorted prefix one position to the right.
- Insert `key` into the resulting gap.

### Pseudocode
```
for i in 1 to n-1:
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key
```

### Time & Space Complexity
| Case | Time | Space |
|---|---|---|
| Best (already sorted) | O(n) | O(1) |
| Average | O(n²) | O(1) |
| Worst (reverse sorted) | O(n²) | O(1) |

### Sample Input / Output
```
Input:  [5, 2, 9, 1, 7, 4]
Output: [1, 2, 4, 5, 7, 9]
```

---

## 4. Insertion Sort (Recursive)

**File:** `recursive_insertion_.py`

### Problem Statement
Same as Insertion Sort above, implemented recursively.

### Algorithm / Approach
- Recursively sort the first `n-1` elements first.
- Once the smaller sub-array is sorted, insert the `n`-th element into its correct position using the standard shift-and-insert logic.
- Base case: an array of size 0 or 1 is already sorted.

### Pseudocode
```
function insertion_sort(arr, n):
    if n <= 1: return
    insertion_sort(arr, n-1)   // sort first n-1 elements
    key = arr[n-1]
    j = n-2
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key
```

### Time & Space Complexity
| Case | Time | Space |
|---|---|---|
| Best | O(n) | O(n) |
| Average | O(n²) | O(n) |
| Worst | O(n²) | O(n) |

Space is O(n) here because of the recursion call stack (n nested calls before any insertion happens), compared to O(1) for the iterative version.

### Sample Input / Output
```
Input:  [5, 2, 4, 1, 3]
Output: Sorted array: [1, 2, 3, 4, 5]
```

---

## 5. Selection Sort

**File:** `selection_sort.py`

### Problem Statement
Sort an array by repeatedly selecting the smallest remaining element and moving it to its correct position.

### Algorithm / Approach
- For each position `i`, scan the remaining unsorted portion of the array to find the index of the minimum element.
- Swap that minimum element into position `i`.
- Repeat until the whole array is traversed.

### Pseudocode
```
for i in 0 to n-2:
    min_index = i
    for j in i+1 to n-1:
        if arr[j] < arr[min_index]:
            min_index = j
    swap(arr[i], arr[min_index])
```

### Time & Space Complexity
| Case | Time | Space |
|---|---|---|
| Best | O(n²) | O(1) |
| Average | O(n²) | O(1) |
| Worst | O(n²) | O(1) |

Unlike Bubble/Insertion sort, Selection Sort has **no best-case improvement** — it always performs the same number of comparisons regardless of initial order, because it scans the full remaining sub-array every time to find the minimum. Its advantage is a minimal number of **swaps** (at most n-1), which makes it useful when write/swap operations are expensive.

### Sample Input / Output
```
Input:  [64, 25, 12, 22, 11]
Output: Sorted array: [11, 12, 22, 25, 64]
```

---

## 6. Linear Search

**File:** `Linear_Search.py`

### Problem Statement
Given an unsorted (or sorted) list and a target value, find the index of the target by checking elements sequentially.

### Algorithm / Approach
- Traverse the list from the first element to the last.
- Compare each element with the target; return its index the moment a match is found.
- If the loop completes without a match, the target is not present.

### Pseudocode
```
for i in 0 to n-1:
    if lst[i] == target:
        return i
return -1
```

### Time & Space Complexity
| Case | Time | Space |
|---|---|---|
| Best (found at index 0) | O(1) | O(1) |
| Average | O(n) | O(1) |
| Worst (not found / last index) | O(n) | O(1) |

### Sample Input / Output
```
Input:  lst = [64, 34, 25, 12, 22, 11, 90], target = 22
Output: Element 22 found at index: 4
```

---

## 7. Binary Search (Iterative)

**File:** `Iterative_Binary_Search.py`

### Problem Statement
Given a **sorted** array and a target value, efficiently find the index of the target by repeatedly halving the search space.

### Algorithm / Approach
- Maintain `low` and `high` pointers spanning the current search range.
- Compute the middle index `mid`.
- If `arr[mid]` equals the target, return `mid`.
- If the target is smaller, discard the right half (`high = mid - 1`); otherwise discard the left half (`low = mid + 1`).
- Repeat until the range is empty (`low > high`), returning -1 if never found.

### Pseudocode
```
low = 0, high = n-1
while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key: return mid
    elif key < arr[mid]: high = mid - 1
    else: low = mid + 1
return -1
```

### Time & Space Complexity
| Case | Time | Space |
|---|---|---|
| Best (mid match) | O(1) | O(1) |
| Average | O(log n) | O(1) |
| Worst | O(log n) | O(1) |

**Precondition:** the input array must be sorted, otherwise the algorithm's correctness breaks down.

### Sample Input / Output
```
Input:  arr = [10, 20, 30, 40, 50, 60, 70], key = 50
Output: element found at index 4
```

---

## 8. Binary Search (Recursive)

**File:** `Recursive_Binary_Search.py`

### Problem Statement
Same as Binary Search above, implemented recursively.

### Algorithm / Approach (as implemented)
- Recursively narrows the search range using `low` and `high` boundaries passed as parameters.
- Base case: if `low > high`, the target isn't in the array → return -1.
- If `arr[mid] == key`, return `mid`.
- If `arr[mid] > key`, recurse into the left half (`high = mid - 1`).
- If `arr[mid] < key`, recurse into the right half.

### Pseudocode (intended binary search)
```
function binary_s(arr, low, high, key):
    if low > high: return -1
    mid = (low + high) // 2
    if arr[mid] == key: return mid
    elif arr[mid] > key: return binary_s(arr, low, mid-1, key)
    else: return binary_s(arr, mid+1, high, key)
```

### ⚠️ Implementation Note
In the uploaded file, the right-recursion call is written as:
```python
return binary_s(arr,low+1, high , key)
```
This increments `low` by only **1** instead of jumping to `mid+1`. The function still returns correct results, but it loses the halving property on the "search right" branch — instead of discarding half the remaining range each time, it only discards one element. This degrades the algorithm's efficiency on the right-side search path toward **O(n)** in the worst case, rather than the expected O(log n). For a true binary search, that line should be `binary_s(arr, mid+1, high, key)`.

### Time & Space Complexity
| Case | Time (as intended) | Time (as implemented) | Space |
|---|---|---|---|
| Best | O(1) | O(1) | O(1) |
| Average | O(log n) | O(n) worst-side | O(log n) |
| Worst | O(log n) | O(n) | O(log n) |

Space is O(log n) (intended) due to the recursion call stack, one frame per halving — or up to O(n) stack depth in the implemented right-search branch, since `low` only advances by 1 per call.

### Sample Input / Output
```
Input:  arr = [10, 20, 30, 40, 50, 60, 70, 80, 90], key = 80
Output: 80 found at index 7
```

---

## Overall Complexity Comparison

| Algorithm | Best | Average | Worst | Space | Stable? | In-place? |
|---|---|---|---|---|---|---|
| Bubble Sort (Iterative) | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Bubble Sort (Recursive) | O(n²) | O(n²) | O(n²) | O(n) | Yes | Yes |
| Insertion Sort (Iterative) | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Insertion Sort (Recursive) | O(n) | O(n²) | O(n²) | O(n) | Yes | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Linear Search | O(1) | O(n) | O(n) | O(1) | — | — |
| Binary Search (Iterative) | O(1) | O(log n) | O(log n) | O(1) | — | — |
| Binary Search (Recursive) | O(1) | O(log n)* | O(log n)* | O(log n) | — | — |

*Assumes the corrected implementation; see the implementation note in Section 8 for the as-uploaded behavior.

---

## Learning Outcomes

Through implementing and analyzing these algorithms, this repository demonstrates:

- **Core sorting techniques** — comparison-based sorting via Bubble, Insertion, and Selection sort, and how their nested-loop structures translate into O(n²) time complexity.
- **Iterative vs. recursive trade-offs** — recursive implementations are often more elegant and closely mirror the mathematical/inductive definition of an algorithm, but introduce O(n) or O(log n) auxiliary space via the call stack, which iterative versions avoid entirely.
- **Early-exit optimizations** — how a simple flag (as in the iterative Bubble Sort) can improve best-case time complexity from O(n²) to O(n) without changing the worst case.
- **Divide-and-conquer searching** — how Binary Search achieves O(log n) time by discarding half the search space each step, and why this requires the input to be pre-sorted.
- **The cost of subtle bugs** — the off-by-one issue in the recursive Binary Search (`low+1` vs `mid+1`) shows how a small implementation error can silently preserve correctness while destroying the algorithm's intended time complexity — a reminder that testing for correct *output* isn't sufficient; complexity must be verified independently (e.g., by counting recursive calls).
- **Space complexity awareness** — recognizing that "space complexity" isn't just about explicit data structures, but also includes implicit memory usage like recursion call stacks.

---

## How to Run

Each file is self-contained and can be run independently:

```bash
python bubble_sort.py
python Recursive_Bubble_Sort.py
python Insertion_Sort.py
python recursive_insertion_.py
python selection_sort.py
python Linear_Search.py
python Iterative_Binary_Search.py
python Recursive_Binary_Search.py
```

**Requirements:** Python 3.x (no external libraries needed).

---

## Repository Structure

```
.
├── bubble_sort.py
├── Recursive_Bubble_Sort.py
├── Insertion_Sort.py
├── recursive_insertion_.py
├── selection_sort.py
├── Linear_Search.py
├── Iterative_Binary_Search.py
├── Recursive_Binary_Search.py
├── Complexity_analyser.py
└── README.md
```    