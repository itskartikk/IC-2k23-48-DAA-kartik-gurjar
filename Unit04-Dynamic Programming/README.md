# Dynamic Programming and Graph Algorithms in Python

## Overview
This repository contains Python 3 implementations of fundamental algorithms based on Recursion, Dynamic Programming, and Graph Theory. These programs demonstrate different problem-solving techniques used in Design and Analysis of Algorithms (DAA).

## Programs Included

| S.No. | Algorithm | Technique |
|---|---|---|
| 1 | Fibonacci using Recursion | Recursion |
| 2 | Fibonacci using Memoization | Dynamic Programming (Top-Down) |
| 3 | 0/1 Knapsack | Dynamic Programming |
| 4 | Multistage Graph | Dynamic Programming |
| 5 | All-Pairs Shortest Path (Floyd-Warshall) | Dynamic Programming |
| 6 | Single-Source Shortest Path (Dijkstra) | Greedy Algorithm |
| 7 | Traveling Salesperson Problem (TSP) | Dynamic Programming (Bitmasking) |

## 1. Fibonacci using Recursion
**Aim:** To generate the Fibonacci series using a recursive approach.

**Description:** Each Fibonacci number is calculated by adding the previous two numbers. The function calls itself until it reaches the base cases (0 and 1).

**Time Complexity:** O(2^n)  
**Space Complexity:** O(n)

## 2. Fibonacci using Memoization
**Aim:** To generate the Fibonacci series using Dynamic Programming and Memoization.

**Description:** Previously calculated Fibonacci values are stored in a dictionary to avoid repeated recursive calculations, improving efficiency.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

## 3. 0/1 Knapsack using Dynamic Programming
**Aim:** To maximize the total value of selected items without exceeding the given knapsack capacity.

**Description:** Each item can either be selected or rejected. A DP table stores the maximum achievable value for different item counts and capacities.

**Time Complexity:** O(n × W)  
**Space Complexity:** O(n × W)

Where:
- n = Number of items
- W = Knapsack capacity

## 4. Multistage Graph
**Aim:** To find the minimum-cost path from the source vertex to the destination vertex in a multistage graph.

**Description:** The graph is divided into multiple stages. Dynamic Programming calculates the minimum cost by processing vertices in reverse order, from destination to source.

**Time Complexity:** O(V²)  
**Space Complexity:** O(V), excluding the adjacency matrix.

## 5. All-Pairs Shortest Path using Floyd-Warshall
**Aim:** To find the shortest distances between every pair of vertices in a weighted graph.

**Description:** The Floyd-Warshall algorithm uses an intermediate vertex to repeatedly update the shortest distance between all pairs of vertices.

**Time Complexity:** O(V³)  
**Space Complexity:** O(V²)

## 6. Single-Source Shortest Path using Dijkstra
**Aim:** To find the shortest distance from a given source vertex to all other vertices in a weighted graph.

**Description:** Dijkstra's algorithm uses a priority queue to select the vertex with the minimum known distance and updates the distances of its adjacent vertices.

**Time Complexity:** O((V + E) log V)  
**Space Complexity:** O(V + E)

**Note:** Dijkstra's algorithm works with non-negative edge weights.

## 7. Traveling Salesperson Problem using Dynamic Programming
**Aim:** To find the minimum-cost tour that visits every city exactly once and returns to the starting city.

**Description:** The algorithm uses Bitmask Dynamic Programming to represent visited cities and calculate the minimum cost of different possible tours.

**Time Complexity:** O(n² × 2ⁿ)  
**Space Complexity:** O(n × 2ⁿ)

## Technologies Used
- Programming Language: Python 3
- Concepts: Recursion, Dynamic Programming, Memoization, Graph Theory, Greedy Algorithms, Bitmasking
- Python Libraries: `heapq` (for Dijkstra's Algorithm)

## How to Run

1. Install Python 3 on your system.
2. Clone the repository or download the source files.
3. Open the project folder in VS Code, PyCharm, or any Python IDE.
4. Run the required Python file:

```bash
python filename.py
```

5. Enter the required input when prompted.
6. View the calculated output in the terminal.

## Learning Outcomes
- Understand recursion and its implementation.
- Learn Top-Down and Dynamic Programming approaches.
- Apply Memoization to optimize recursive algorithms.
- Solve optimization problems using 0/1 Knapsack.
- Understand shortest-path algorithms in graphs.
- Implement the Floyd-Warshall and Dijkstra algorithms.
- Solve the Traveling Salesperson Problem using Bitmask DP.
- Analyze the time and space complexities of algorithms.
