# Sorting Algorithms & Majority Element Analysis

This project was developed for the CSE2246 "Analysis of Algorithms" course, Spring 2025. It focuses on comparing multiple algorithmic strategies for solving the **FindMajority** problem — determining whether a majority element exists in an array, and identifying it if it does.

## 🧠 Problem Definition

A **majority element** in an array `A[1..n]` is an element that appears more than `⌊n/2⌋` times. The task is to design and empirically compare various algorithms that return the majority element, or `-1` if there is none.

---

## 🚀 Implemented Algorithms

The following algorithms were implemented and tested for performance:

1. **Brute Force** – Double loop counting occurrences.
2. **Insertion Sort + Median** – Sort with insertion sort, return `⌈n/2⌉`-th element.
3. **Merge Sort + Median**
4. **Quick Sort + Median** – Pivot is the first element.
5. **Divide & Conquer** – Recursive strategy without sorting.
6. **Hashing-based** – Using a hash map to track frequencies.
7. **Boyer-Moore Majority Voting** – Efficient linear-time solution.
8. **Bitwise Majority Algorithm** – Custom method using bit-level operations (extension).

---

## 🧪 Experiment Design

- **Input Types:** Best, average, and worst-case arrays were generated to reflect real-world performance, including arrays with no majority, clear majority, and borderline cases.
- **Array Sizes:** Ranging from small to large.
- **Metrics:** operation count (e.g., comparisons) recorded for analysis.

---

## 📊 Results & Evaluation

- Visualizations include comparison plots of exact operation counts and asymptotic complexities.
- Additional ratio plots illustrate the consistency between theoretical expectations and actual performance.
- All methods were benchmarked on the same machine for consistency.

---

## 📁 Repository Structure

- `sortingAlgorithms.py`: Main Python script including the implementation of all majority element algorithms.
- `analysis.xlsx`: Analysis output in Excel format, including performance metrics like operation counts.
- `output.txt`: Same analysis results as in the Excel file, provided in plain text format for quick access and sharing.

---

## 👨‍💻 Contribution

This project was collaboratively developed by:

- [Ahmet Salih Yaman](https://github.com/ahmetyaman16): Implemented the majority of the algorithms(Brute Force - Merge Sort), designed test cases, and handled performance analysis.
- [Elman Kakharmanov](https://github.com/Elllmaan): Contributed to the implementation of sorting-based approaches and prepared the data visualization and graphs.
- [Esma Nur Gezi](https://github.com/esmagezi): Worked on experiment design, prepared the final report, and assisted in implementing hash-based and Boyer-Moore algorithms.

All members participated in result evaluation and final documentation.

---

## 📜 References

- [Boyer-Moore Voting Algorithm – Wikipedia](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm)
- CSE2246 Lecture Notes, Spring 2025
