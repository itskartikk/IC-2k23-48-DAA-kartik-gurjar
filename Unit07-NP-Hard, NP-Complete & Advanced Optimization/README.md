# Exhaustive Search and Branch and Bound in Python

## Overview

This repository contains Python 3 implementations of Exhaustive Search and Branch and Bound algorithms used in Design and Analysis of Algorithms (DAA).

These techniques are used to solve optimization problems by exploring possible solutions and identifying the best feasible result.

## Programs Included

| S.No. | Program | Technique |
|---|---|---|
| 1 | Small Problem using Exhaustive Search | Exhaustive Search |
| 2 | 0/1 Knapsack | Branch and Bound |
| 3 | Traveling Salesperson Problem (TSP) | Branch and Bound |

## 1. Small Problem using Exhaustive Search

**Aim:** To demonstrate the Exhaustive Search technique by finding the maximum-sum subset without exceeding a given capacity.

**Description:** The program generates all possible subsets of the given array, calculates their sums, and selects the subset with the maximum sum that satisfies the capacity constraint.

**Time Complexity:** O(n × 2ⁿ)

**Space Complexity:** O(n), excluding input storage.

## 2. 0/1 Knapsack using Branch and Bound

**Aim:** To maximize the total profit of selected items without exceeding the knapsack capacity using Branch and Bound.

**Description:** The algorithm explores possible item selections using a state-space tree. It calculates an upper bound using the Fractional Knapsack approach and prunes branches that cannot produce a better solution than the current maximum profit.

**Time Complexity:** O(2ⁿ) worst case, plus O(n log n) sorting.

**Space Complexity:** O(2ⁿ) worst case.

## 3. Traveling Salesperson Problem using Branch and Bound

**Aim:** To find the minimum-cost tour that visits every city exactly once and returns to the starting city.

**Description:** The algorithm explores possible routes using Branch and Bound. It calculates a lower bound for each partial route and eliminates routes that cannot produce a better solution than the current minimum-cost tour.

**Time Complexity:** O(n!) worst case.

**Space Complexity:** O(n) auxiliary recursion and path space, excluding the cost matrix.

## Technologies Used

- Programming Language: Python 3
- Concepts: Exhaustive Search, Branch and Bound, Recursion, Optimization, State Space Tree, Pruning
- Python Libraries: `heapq` (used in 0/1 Knapsack)

## How to Run

1. Install Python 3 on your system.
2. Clone the repository or download the source files.
3. Open the project folder in VS Code, PyCharm, or any Python IDE.
4. Run the required Python file:

```bash
python filename.py
```

5. Enter the required input when prompted.
6. View the result in the terminal.

## Learning Outcomes

- Understand the Exhaustive Search technique.
- Learn how to generate and evaluate all possible solutions.
- Understand the Branch and Bound technique.
- Learn the concepts of branching, bounding, and pruning.
- Solve the 0/1 Knapsack optimization problem.
- Implement the Traveling Salesperson Problem using Branch and Bound.
- Understand the State Space Tree representation.
- Analyze the time and space complexities of optimization algorithms.