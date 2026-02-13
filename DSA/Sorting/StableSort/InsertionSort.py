def insertion_sort(arr):
    # Traverse the array starting from index 1
    # (First element is already considered sorted)
    for i in range(len(arr) - 1):

        # Start comparing the next element with elements in the sorted portion
        # Move backwards to place it at its correct position
        for j in range(i + 1, 0, -1):

            # If current element is smaller than the previous one,
            # swap them to move it left
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                # If no swap is needed, the element is in correct position
                # Since left side is already sorted, we can stop early
                break

    return arr


if __name__ == "__main__":
    nums = [2, -32, 0, 78, 1]
    print(insertion_sort(nums))
