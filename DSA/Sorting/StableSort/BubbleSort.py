def bubble_sort(arr):
    # Run the outer loop n-1 times.
    # After each pass, the largest unsorted element gets placed at its correct position at the end.
    for i in range(len(arr) - 1):
        is_swapped = False

        # In each pass, compare adjacent elements up to the unsorted portion.
        # The last i elements are already sorted, so we ignore them.
        for j in range(1, len(arr) - i):
            if arr[j - 1] > arr[j]:
                # Swap adjacent elements if they are in the wrong order
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                is_swapped = True

        # If no swaps occurred in this pass,
        # the array is already sorted, so we can stop early.
        if not is_swapped:
            return arr

    return arr


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]
    print(bubble_sort(nums))
