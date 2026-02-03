def binary_search(arr, target):
    """
    Returns the index of target in a sorted array using binary search, or -1 if not found.
    O(log N)
    """

    # Pointers
    start, end = 0, len(arr) - 1

    while start <= end:
        # Find the middle element
        mid = start + (end - start) // 2  # As python doesn't have a fixed range doing simple mid calc is fine.

        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            # Answer found
            return mid

    return -1


if __name__ == "__main__":
    arr = [-18, -12, -4, 0, 2, 3, 4, 5, 15, 16, 18, 22, 45, 89]
    target = 1000
    ans = binary_search(arr, target)
    print(ans)
