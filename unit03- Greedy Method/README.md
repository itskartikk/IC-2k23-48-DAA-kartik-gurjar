# Design and Analysis of Algorithms (DAA) – Greedy Algorithms

This repository contains Python implementations of four important Greedy Algorithm problems studied in Design and Analysis of Algorithms (DAA).

These practicals demonstrate how greedy strategies can be used to solve optimization problems by making locally optimal choices at each step.

## 📂 Practical List

| No. | Practical | Description |
|---|---|---|
| 1 | Fractional Knapsack | Maximizes total profit by selecting items fully or partially based on their profit-to-weight ratio. |
| 2 | Job Sequencing with Deadlines | Schedules jobs within their deadlines to maximize total profit. |
| 3 | Prim's Algorithm | Finds the Minimum Spanning Tree (MST) by repeatedly selecting the minimum-weight edge connecting selected and unselected vertices. |
| 4 | Kruskal's Algorithm | Finds the Minimum Spanning Tree by selecting edges in increasing order of weight while avoiding cycles. |

## 🛠️ Technologies Used

- Python 3
- Built-in Python data structures
- Greedy Algorithm
- Graph Algorithms
- Disjoint Set Union (Union-Find)

## 📁 Project Structure

```text
DAA-Greedy-Algorithms/
│
├── Fractional Knapsack.py
├── Job Sequencing with Deadlines.py
├── Prim's Algorithm.py
├── Kruskal's Algorithm.py
└── README.md
```

## ⚙️ Installation

No external libraries are required.

Make sure Python 3 is installed on your system.

Check Python installation:

```bash
python --version
```

## ▶️ How to Run

Run each practical separately using Python:

### 1. Fractional Knapsack

```bash
python "Fractional Knapsack.py"
```

**Concepts Covered:**
- Greedy approach
- Profit-to-weight ratio
- Sorting in descending order
- Fractional item selection
- Maximum profit calculation

### 2. Job Sequencing with Deadlines

```bash
python "Job Sequencing with Deadlines.py"
```

**Concepts Covered:**
- Greedy job scheduling
- Profit-based sorting
- Deadline management
- Time slot allocation
- Profit maximization

### 3. Prim's Algorithm

```bash
python "Prim's Algorithm.py"
```

**Concepts Covered:**
- Minimum Spanning Tree (MST)
- Weighted undirected graphs
- Adjacency matrix representation
- Minimum edge selection
- Cycle-free spanning tree construction

### 4. Kruskal's Algorithm

```bash
python "Kruskal's Algorithm.py"
```

**Concepts Covered:**
- Minimum Spanning Tree (MST)
- Edge sorting by weight
- Disjoint Set Union (DSU)
- Union-Find data structure
- Path compression
- Union by rank
- Cycle detection

## 📊 Algorithm Complexity

| Algorithm | Time Complexity |
|---|---|
| Fractional Knapsack | O(n log n) |
| Job Sequencing with Deadlines | O(n log n + n × D), where D is the maximum deadline |
| Prim's Algorithm | O(V²) |
| Kruskal's Algorithm | O(E log E) |

Where:
- `n` = Number of items or jobs
- `V` = Number of vertices
- `E` = Number of edges
- `D` = Maximum job deadline

## 🎯 Learning Outcomes

After completing these practicals, you will understand:

- The working principle of Greedy Algorithms.
- How to solve optimization problems using greedy strategies.
- How to maximize profit using Fractional Knapsack.
- How to schedule jobs based on deadlines and profits.
- How to construct a Minimum Spanning Tree.
- The difference between Prim's and Kruskal's algorithms.
- How Union-Find helps in cycle detection.
- How to analyze algorithm time complexity.