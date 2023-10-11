def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # Flag to check if any swaps were made in this pass
        swapped = False

        # Last i elements are already in place, so no need to compare them
        for j in range(0, n - i - 1):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped in this pass, the array is already sorted
        if not swapped:
            break

# Example usage:
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)

print("Sorted array:", my_list)
