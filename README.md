# MSCS-532-M80_Assignment6: Data Structures and Selection Algorithms Implementation

This project implements fundamental data structures and selection algorithms in Python. It demonstrates arrays, matrices, stacks, queues, linked lists, and optionally rooted trees, along with their operations such as insertion, deletion, and traversal. The project also analyzes the performance of these structures and compares deterministic and randomized selection algorithms on different input arrays.

---

## Features

### 1. Data Structures

* **Arrays:** Dynamic arrays supporting insertion, deletion, and indexing.
* **Stacks and Queues:** Implemented using arrays with LIFO and FIFO operations.
* **Linked Lists:** Singly linked lists with operations such as insertion, deletion, and traversal.
* **Rooted Trees (Optional):** Trees implemented using linked lists for node relationships.

### 2. Performance Analysis

* Time complexity analysis of basic operations for each data structure.
* Trade-offs between arrays and linked lists for stacks and queues.
* Efficiency comparison for different data structures under specific scenarios.

---

## Summary of Findings

### Part 1: Selection Algorithms

* **Randomized Selection (Quickselect)** is very fast on average, especially for random and moderately structured arrays, due to low overhead and cache-friendly operations. However, it can fail or degrade on arrays with all equal elements, reflecting its rare O(n²) worst-case scenario.
* **Deterministic Selection (Median of Medians)** consistently achieves O(n) worst-case time, handling all input distributions reliably, including edge cases like “all equal” arrays, though it has higher runtime due to extra median computations.
* **Input Distribution Impact:** Randomized selection excels for random and few-unique inputs, while deterministic selection provides stable performance across all distributions. Empirical results closely match theoretical expectations for time and space complexity.

### Part 2: Elementary Data Structures

* **Arrays and Matrices:** Offer fast random access (O(1)) and cache efficiency, but insertion and deletion in the middle are expensive.
* **Stacks and Queues:** Array-based implementations provide efficient push/pop/enqueue/dequeue with amortized O(1) time; circular arrays improve queue performance. Linked lists are preferable for dynamic sizes or frequent insertions/deletions at the head.
* **Singly Linked Lists:** Provide efficient insertions/deletions at the head but slow random access and poor cache locality. Best when middle or head modifications are frequent.
* **Rooted Trees:** Efficiently represent hierarchical data with O(n) traversal operations; memory overhead arises from storing pointers.
* **Trade-offs:** Arrays excel for speed and memory locality; linked lists for flexibility in dynamic operations; trees for hierarchical data. Choice depends on memory constraints, speed requirements, and the type of operations most frequently performed.

**Overall Conclusion:** Selecting the right data structure or selection algorithm requires balancing theoretical guarantees, practical runtime, memory usage, and input characteristics to optimize performance for specific scenarios.

---

## How to Run

### Requirements

* Python 3.x
* matplotlib (for plotting)

### Install Dependencies

```bash
pip install matplotlib
```

### Running Scripts

**1. Data Structures Demonstration**

```bash
python DSImplementation.py
```

Shows insertion, deletion, traversal, and operations for all implemented data structures.

**2. Selection Algorithms Comparison**

```bash
python SelectionAlgorithm.py
```

Runs randomized and deterministic selection algorithms on multiple test cases, prints execution times, and plots comparative graphs.

---

## Test Inputs

* Random input
* Sorted input
* Reverse sorted input
* All equal elements
* Few unique elements

---
