def order_agnostic_bs(arr, target):
    """
    Returns the index of target in a sorted array (ascending or descending), or -1 if not found.
    O(log N)
    """

    # Pointers
    start, end = 0, len(arr) - 1

    # Find whether the array is sorted in ascending or descending order
    is_asc = arr[start] < arr[end]

    while start <= end:
        # Find the middle element
        mid = start + (end - start) // 2  # As python doesn't have a fixed range doing simple mid calc is fine.

        if target == arr[mid]:
            # Answer found
            return mid

        if is_asc:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

    return -1


if __name__ == "__main__":
    arr = [10, 9, 8, 6, 2, -1, -90]
    target = 100
    print(order_agnostic_bs(arr, target))
