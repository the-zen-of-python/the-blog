def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap adjacent elements if they are out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


numbers = [5, 2, 4, 6, 1, 3]
print(bubble_sort(numbers))
