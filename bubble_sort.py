def bubble_sort(arr):
    n = len(arr)
    # Outer loop for passes
    for i in range(n - 1):
        # Inner loop for comparisons
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example usage
nums = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", nums)
sorted_nums = bubble_sort(nums)
print("Sorted list:", sorted_nums)
