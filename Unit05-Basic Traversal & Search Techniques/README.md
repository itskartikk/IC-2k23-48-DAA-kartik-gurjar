# Binary Tree and Tree Traversals in Python

## Overview

This repository contains Python 3 implementations of Binary Tree Creation and different Tree Traversal techniques. It demonstrates how binary trees are constructed and how their nodes are visited using recursive and iterative approaches.

## Programs Included

| S.No. | Program | Technique |
|---|---|---|
| 1 | Binary Tree Creation | Recursion |
| 2 | Preorder Traversal | Recursive |
| 3 | Inorder Traversal | Recursive |
| 4 | Postorder Traversal | Recursive |
| 5 | Recursive Tree Traversal | Recursion |
| 6 | Iterative Tree Traversal | Stack |

## 1. Binary Tree Creation

**Aim:** To create a binary tree using Python.

**Description:** A binary tree is a hierarchical data structure in which each node can have at most two children: a left child and a right child. The program creates a binary tree using recursive function calls.

**Time Complexity:** O(n)

**Space Complexity:** O(h)

## 2. Preorder Traversal

**Aim:** To perform Preorder Traversal of a binary tree.

**Description:** Preorder traversal visits the root node first, followed by the left subtree and then the right subtree.

**Order:** Root → Left → Right

**Time Complexity:** O(n)

**Space Complexity:** O(h)

## 3. Inorder Traversal

**Aim:** To perform Inorder Traversal of a binary tree.

**Description:** Inorder traversal first visits the left subtree, then the root node, and finally the right subtree.

**Order:** Left → Root → Right

**Time Complexity:** O(n)

**Space Complexity:** O(h)

## 4. Postorder Traversal

**Aim:** To perform Postorder Traversal of a binary tree.

**Description:** Postorder traversal visits the left subtree first, followed by the right subtree, and finally the root node.

**Order:** Left → Right → Root

**Time Complexity:** O(n)

**Space Complexity:** O(h)

## 5. Recursive Tree Traversal

**Aim:** To implement Preorder, Inorder, and Postorder traversals using recursion.

**Description:** Recursive traversal uses function calls to visit each node of the binary tree. The function calls itself for the left and right subtrees until it reaches a NULL node.

**Time Complexity:** O(n) per traversal.

**Space Complexity:** O(h)

## 6. Iterative Tree Traversal

**Aim:** To implement Preorder, Inorder, and Postorder traversals without recursion.

**Description:** Iterative traversal uses an explicit stack data structure instead of recursive function calls. It performs the same traversal operations while managing node visits manually.

**Time Complexity:** O(n) per traversal.

**Space Complexity:** O(n) in the worst case.

## Sample Binary Tree

The following binary tree is used in the traversal programs:

```text
        1
       / \
      2   3
     / \
    4   5
```

### Traversal Outputs

| Traversal | Output |
|---|---|
| Preorder | 1 2 4 5 3 |
| Inorder | 4 2 5 1 3 |
| Postorder | 4 5 2 3 1 |

## Technologies Used

- Programming Language: Python 3
- Concepts: Binary Trees, Recursion, Iteration, Stack, Tree Traversal
- Data Structures: Nodes, Pointers (object references), Stack

## How to Run

1. Install Python 3 on your system.
2. Clone the repository or download the source files.
3. Open the project folder in VS Code, PyCharm, or any Python IDE.
4. Run the required Python file:

```bash
python filename.py
```

5. Enter the required input if prompted.
6. View the traversal output in the terminal.

## Learning Outcomes

- Understand Binary Tree data structures.
- Learn how to create and link tree nodes.
- Understand recursive tree traversal.
- Implement Preorder, Inorder, and Postorder traversals.
- Understand the difference between recursive and iterative approaches.
- Learn how stacks are used in iterative tree traversal.
- Analyze the time and space complexity of tree operations.