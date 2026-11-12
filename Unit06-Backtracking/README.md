# Backtracking Algorithms in Python

## Overview

This repository contains Python 3 implementations of fundamental Backtracking algorithms used in Design and Analysis of Algorithms (DAA).

Backtracking is an algorithmic technique that solves problems by building solutions incrementally. Whenever a partial solution cannot lead to a valid complete solution, the algorithm abandons that possibility and explores another alternative.

## Programs Included

| S.No. | Program | Technique |
|---|---|---|
| 1 | General Backtracking Technique | Recursive Backtracking |
| 2 | 4-Queens Problem | Backtracking |
| 3 | 8-Queens Problem | Backtracking |
| 4 | N-Queens Problem | Generalized Backtracking |
| 5 | Sum of Subsets | Backtracking with Pruning |

## 1. General Backtracking Technique

**Aim:** To implement the general Backtracking technique for solving constraint-based problems.

**Description:** The algorithm builds a solution step by step. It checks whether each selected choice satisfies the required constraints. If a choice is invalid or cannot produce a complete solution, it removes that choice and tries another possibility.

**Time Complexity:** Problem-dependent.

**Space Complexity:** O(d), where d is the recursion depth.

## 2. 4-Queens Problem

**Aim:** To place four queens on a 4×4 chessboard such that no two queens attack each other.

**Description:** The program places one queen in each row. Before placing a queen, it checks whether the selected column and diagonals are safe. If no valid position is available, it backtracks and changes the previous queen's position.

**Time Complexity:** O(N!) with pruning, ignoring safety-check overhead.

**Space Complexity:** O(N) auxiliary space.

## 3. 8-Queens Problem

**Aim:** To place eight queens on an 8×8 chessboard without any two queens attacking each other.

**Description:** The program uses recursive Backtracking to find a valid arrangement of eight queens. It checks column and diagonal conflicts before placing each queen.

**Time Complexity:** O(N!) with pruning, ignoring safety-check overhead.

**Space Complexity:** O(N) auxiliary space.

## 4. N-Queens Problem

**Aim:** To solve the generalized N-Queens problem for any positive value of N.

**Description:** The algorithm places N queens on an N×N chessboard. It ensures that no two queens occupy the same column or diagonal. The program explores possible arrangements using recursive Backtracking and counts all valid solutions.

**Time Complexity:** O(N!) with pruning, ignoring safety-check overhead.

**Space Complexity:** O(N) auxiliary space, excluding stored solutions.

## 5. Sum of Subsets

**Aim:** To find all subsets of a given set whose sum equals a specified target value.

**Description:** The algorithm explores two possibilities for each element: including it in the current subset or excluding it. Backtracking is used to explore these choices, while pruning eliminates branches whose current sum exceeds the target.

**Time Complexity:** O(2ⁿ) worst case, excluding output formatting.

**Space Complexity:** O(n) auxiliary recursion space, excluding stored solutions.

**Note:** The implementation accepts positive integers and avoids duplicate subsets.

## Technologies Used

- Programming Language: Python 3
- Concepts: Backtracking, Recursion, State Space Tree, Constraint Satisfaction, Pruning
- Data Structures: Lists, Arrays, Recursive Function Calls

## How to Run

1. Install Python 3 on your system.
2. Clone the repository or download the source files.
3. Open the project folder in VS Code, PyCharm, or any Python IDE.
4. Run the required Python file:

```bash
python filename.py
```

5. Enter the required input when prompted.
6. View the generated solutions in the terminal.

## Learning Outcomes

- Understand the Backtracking algorithmic technique.
- Learn how to build solutions incrementally.
- Understand the concept of a State Space Tree.
- Apply Backtracking to constraint satisfaction problems.
- Solve the 4-Queens and 8-Queens problems.
- Generalize the N-Queens problem for any board size.
- Find subsets satisfying a given sum using Backtracking.
- Understand pruning and its role in reducing unnecessary computation.
- Analyze the time and space complexities of Backtracking algorithms.
