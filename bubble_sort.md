# Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly compares
adjacent elements and swaps them when they are in the wrong order.

## How the algorithm works

Given the list:

```text
[5, 2, 4, 6, 1, 3]
```

Bubble Sort works by comparing neighboring elements:

1. Compare the first two elements.
2. If the left element is greater than the right element, swap them.
3. Move to the next pair of adjacent elements.
4. Continue until the end of the list is reached.
5. After one complete pass, the largest unsorted element will have moved
   ("bubbled") to the end.
6. Repeat the process for the remaining unsorted elements.

For example, during the first pass:

```text
[5, 2, 4, 6, 1, 3]

[5, 2] -> swap -> [2, 5, 4, 6, 1, 3]
[5, 4] -> swap -> [2, 4, 5, 6, 1, 3]
[5, 6] -> no swap
[6, 1] -> swap -> [2, 4, 5, 1, 6, 3]
[6, 3] -> swap -> [2, 4, 5, 1, 3, 6]
```

The largest element, `6`, is now in its correct position at the end.

The process continues until the entire list is sorted:

```text
[1, 2, 3, 4, 5, 6]
```

## Python implementation

See `bubble_sort.py` for the implementation.

## Complexity

### Time complexity

- **Best case:** `O(n)` with an optimized implementation when the list is already sorted.
- **Average case:** `O(n²)`
- **Worst case:** `O(n²)`

The simple implementation in `bubble_sort.py` does not include the
early-exit optimization, so its best-case time is also `O(n²)`.

### Space complexity

- **O(1)** extra space.

Bubble Sort sorts the list in place and does not require another list
proportional to the input size.

## Key idea

> Compare adjacent elements and swap them when they are out of order.
> After each pass, the largest remaining element bubbles to the end.
